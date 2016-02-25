function [delta,beta]=HE_PMMA_delta_beta(E)
%% SiO2_delta_beta
% 
% DESCRIPTION:
%   PMMA delta and beta values as function of the energy
%   Density assumed rho=1.19 g/cm3
%
%
%%
table=[1000.00,  0.000276929, 3.29400e-05;
      2000.00,  6.84524e-05, 2.37938e-06;
      3000.00,  3.01113e-05, 4.88338e-07;
      4000.00,  1.68453e-05, 1.54971e-07;
      5000.00,  1.07463e-05, 6.26494e-08;
      6000.00,  7.44749e-06, 2.96870e-08;
      7000.00,  5.46410e-06, 1.57101e-08;
      8000.00,  4.17939e-06, 9.01766e-09;
      9000.00,  3.29988e-06, 5.50841e-09;
      10000.0,  2.67146e-06, 3.53683e-09;
      11000.0,  2.20690e-06, 2.36380e-09;
      12000.0,  1.85379e-06, 1.63332e-09;
      13000.0,  1.57914e-06, 1.16118e-09;
      14000.0,  1.36131e-06, 8.45918e-10;
      15000.0,  1.18564e-06, 6.29285e-10;
      16000.0,  1.04191e-06, 4.76946e-10;
      17000.0,  9.22816e-07, 3.67555e-10;
      18000.0,  8.23039e-07, 2.87429e-10;
      19000.0,  7.38613e-07, 2.27856e-10;
      20000.0,  6.66544e-07, 1.83175e-10;
      21000.0,  6.04532e-07, 1.48438e-10;
      22000.0,  5.50789e-07, 1.21406e-10;
      23000.0,  5.03908e-07, 1.00211e-10;
      24000.0,  4.62768e-07, 8.33967e-11;
      25000.0,  4.26468e-07, 6.99611e-11;
      26000.0,  3.94278e-07, 5.90876e-11;
      27000.0,  3.65600e-07, 5.02461e-11;
      28000.0,  3.39942e-07, 4.29772e-11;
      29000.0,  3.16893e-07, 3.69632e-11;
      30000.0,  2.96111e-07, 3.19566e-11;
      31000.0,  2.77307e-07, 2.92362e-11;
      32000.0,  2.60242e-07, 2.55152e-11;
      33000.0,  2.44704e-07, 2.23538e-11;
      34000.0,  2.30516e-07, 1.96680e-11;
      35000.0,  2.17528e-07, 1.73710e-11;
      36000.0,  2.05607e-07, 1.53838e-11;
      37000.0,  1.94641e-07, 1.36734e-11;
      38000.0,  1.84529e-07, 1.21922e-11;
      39000.0,  1.75185e-07, 1.09039e-11;
      40000.0,  1.66533e-07, 9.77932e-12;
      41000.0,  1.58507e-07, 8.79820e-12;
      42000.0,  1.51048e-07, 7.93127e-12;
      43000.0,  1.44103e-07, 7.16262e-12;
      44000.0,  1.37626e-07, 6.49093e-12;
      45000.0,  1.31576e-07, 5.89228e-12;
      46000.0,  1.25916e-07, 5.35693e-12;
      47000.0,  1.20614e-07, 4.88270e-12;
      48000.0,  1.15640e-07, 4.45914e-12;
      49000.0,  1.10967e-07, 4.07995e-12;
      50000.0,  1.06573e-07, 3.73971e-12;
      51000.0,  1.02434e-07, 3.43547e-12;
      52000.0,  9.85313e-08, 3.15750e-12;
      53000.0,  9.48477e-08, 2.90995e-12;
      54000.0,  9.13669e-08, 2.68301e-12;
      55000.0,  8.80743e-08, 2.48003e-12;
      56000.0,  8.49564e-08, 2.29337e-12;
      57000.0,  8.20013e-08, 2.12544e-12;
      58000.0,  7.91977e-08, 1.97134e-12;
      59000.0,  7.65355e-08, 1.83152e-12;
      60000.0,  7.40052e-08, 1.70290e-12;];
    
    
E_tab=table(:,1)*1e-3;%keV
delta_tab=table(:,2);
beta_tab=table(:,3);

delta=interp1(E_tab,delta_tab,E,'pchip');
beta=interp1(E_tab,beta_tab,E,'pchip');    
end
     
