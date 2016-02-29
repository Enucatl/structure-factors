import numpy as np
import scipy
import logging

log = logging.getLogger(__name__)


def sphere_form_factor(q, d):
    """
    Function to calculate the sphere form factor for different radii hard
    spheres
    D.J. Kinning et al., Macromolecules 17 (1984) 1712

    :q: 4*pi/lambda*sin(theta/2)
    :d: diameter of the microspheres
    """
    a = q * d / 2
    form_factor = 3 / a ** 3 * (np.sin(a) - a * np.cos(a))
    form_factor[a == 0] = 1 / 3
    return form_factor


def g(a, f):
    alpha = ((1 + 2 * f) ** 2) / ((1 - f) ** 4)
    beta = -6 * f * (1 + (f / 2)) ** 2 / (1 - f) ** 4
    gamma = 0.5 * f * (1 + (2 * f) ** 2) / (1 - f) ** 4

    result = (
        alpha / (a ** 2) * (np.sin(a) - (a * np.cos(a))) +
        beta / (a ** 3) * ((2 * a * np.sin(a)) +
                           ((2 - (a ** 2)) * np.cos(a)) - 2) +
        gamma / (a ** 5) * (((-a ** 4) * np.cos(a)) +
                            (4 * (((3 * a ** 2 - 6) * np.cos(a)) +
                                  (np.sin(a) * (a ** 3 - 6 * a)) + 6)))
    ) / a
    result[a == 0] = alpha / 3 + beta / 4 + gamma / 6
    return result


def hard_sphere_structure_factor(q, d, f):
    """
    Function to calculate structure factors for different radii hard spheres
    D.J. Kinning et al., Macromolecules 17 (1984) 1712

    :q: 4*pi/lambda*sin(theta/2)
    :d: diameter of the microspheres
    :f: fraction volume
    """
    return 1 / (1 + (24 * f * g(q * d, f)))


def dark_field_extinction_coefficient(
        wavelength,
        grating_pitch,
        intergrating_distance,
        diameter,
        volume_fraction,
        delta_chi_squared,
        real_space_sampling):
    """TODO: Docstring for autocorrelation.
    # n = even

    :arg1: TODO
    :returns: TODO

    """

    autocorrelation_length = wavelength * intergrating_distance / grating_pitch
    sampling_step = real_space_sampling[1] - real_space_sampling[0]
    log.debug("sampling step %g", sampling_step)
    n = len(real_space_sampling)
    log.debug("sampling cells %g", n)
    log.debug("real space sampling %s", real_space_sampling)
    fourier_sampling_step = 1 / (n * sampling_step)
    log.debug("fourier sampling step %g", fourier_sampling_step)
    fourier_space_sampling = np.linspace(
        -n / (16 * autocorrelation_length),
        n / (16 * autocorrelation_length),
        n,
        endpoint=False,
    )
    log.debug("fourier space sampling %s", fourier_space_sampling)
    fx, fy = np.meshgrid(fourier_space_sampling, fourier_space_sampling)
    f = np.sqrt(fx ** 2 + fy ** 2)
    q = 2 * np.pi * f

    sphere_factor = sphere_form_factor(q, diameter) ** 2
    log.debug("sphere form factor %s", sphere_factor)
    structure_factor = 1

    intensity = (
        volume_fraction *
        delta_chi_squared *
        np.pi * diameter ** 3 / 6 *
        sphere_factor * structure_factor
    )
    log.debug("intensity \n %s", intensity)

    k = 2 * np.pi / wavelength
    log.debug("k \n %g", k)
    autocorrelation = (
        k ** 2 *
        np.fft.fftshift(np.real(np.fft.ifft2(np.fft.ifftshift(intensity)))) /
        sampling_step ** 2
    )
    log.debug("autocorrelation \n %s", autocorrelation)

    autocorrelation_sampling = np.fft.ifftshift(real_space_sampling)
    autocorrelation_values = np.fft.ifftshift(autocorrelation)[0, :]
    autocorrelation1 = scipy.interpolate.interp1d(
        autocorrelation_sampling,
        autocorrelation_values
    )(autocorrelation_length)
    log.debug("autocorrelation length \n %s", autocorrelation_length)
    log.debug("autocorrelation sampling \n %s", autocorrelation_sampling)
    log.debug("autocorrelation values \n %s", autocorrelation_values)
    log.debug("autocorrelation1 %g", autocorrelation1)

    dfec = autocorrelation_values[0] - autocorrelation1
    log.debug("saxs dfec %g", dfec)
    return dfec
