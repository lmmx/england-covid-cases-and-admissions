# england-covid-cases-and-admissions

- [x] Plot of COVID cases and hospital admissions in England
  - Absolute; rolling rates; and percentage of historic peaks
- [x] Plot of COVID cases and hospital admissions in England alongside COVID variant presence
  - [Overlay of Omicron (SGTF) prevalence](plot_rolling_cases_and_admissions_omicron.py);
  - [overlay of 'dual epidemics'](plot_rolling_cases_and_admissions_omicron_vs_delta.py);
  - [detail view of last 6 months](plot_rolling_cases_and_admissions_omicron_vs_delta_last_6_months.py);
  - [detail view of December 2021 Omicron wave](plot_rr_cases_deaths_admissions_omicron_wave.py)

![](https://raw.githubusercontent.com/lmmx/england-covid-cases-and-admissions/master/plots/rolling_cases_abs_and_admissions.png)
![](https://raw.githubusercontent.com/lmmx/england-covid-cases-and-admissions/master/plots/rolling_cases_percentage_and_admissions.png)
![](https://raw.githubusercontent.com/lmmx/england-covid-cases-and-admissions/master/plots/rolling_cases_percentage_and_admissions_with_sgtf.png)
![](https://raw.githubusercontent.com/lmmx/england-covid-cases-and-admissions/master/plots/rolling_cases_percentage_and_admissions_omicron_vs_delta.png)
![](https://raw.githubusercontent.com/lmmx/england-covid-cases-and-admissions/master/plots/rolling_cases_percentage_and_admissions_omicron_vs_delta_6_months.png)
![](https://raw.githubusercontent.com/lmmx/england-covid-cases-and-admissions/master/plots/rolling_cases_percentage_and_admissions_omicron_vs_delta_from_dec_2021.png)

- `data/ukhsa_national_covid_case_rates_and_admissions.csv` came from
  [source CSV](https://api.coronavirus.data.gov.uk/v2/data?areaType=nation&areaCode=E92000001&metric=newAdmissions&metric=newCasesBySpecimenDate&format=csv)
  via [nicfreeman1209 on GitHub](https://github.com/nicfreeman1209/covid-19/blob/main/conv-estimator/conv_estimator_direct.ipynb)
  originally via [Nic Freeman](https://twitter.com/nicfreeman1209/status/1472966382719574023)
  on 21st December 2021
- `data/ukhsa_national_covid_case_rates_deaths_admissions_rolling_rates.csv` came from 
  [source CSV](https://api.coronavirus.data.gov.uk/v2/data?areaType=nation&areaCode=E92000001&metric=newAdmissionsRollingRate&metric=newCasesBySpecimenDateRollingRate&metric=newDeaths28DaysByDeathDateRollingRate&format=csv)
  and was deliberately chosen to use rolling rates for all metrics
- `data/ukhsa_sgtf_totalepicurve_2021-12-20-1.csv` came from
  [source CSV](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1042753/sgtf_totalepicurve_2021-12-20-1.csv)
  via [Omicron daily overview](https://www.gov.uk/government/publications/covid-19-omicron-daily-overview)
  and the CSV can be [previewed online here](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1042753/sgtf_totalepicurve_2021-12-20-1.csv/preview)
  originally via [Oliver Johnson](https://twitter.com/BristOliver/status/1473359880329351169)
