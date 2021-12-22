import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

ukhsa_national_rr_csv = "data/ukhsa_national_covid_case_rates_deaths_admissions_rolling_rates.csv"
ukhsa_omicron_sgtf_csv = "data/ukhsa_sgtf_totalepicurve_2021-12-20-1.csv"

adm_case_df = pd.read_csv(ukhsa_national_rr_csv)
adm_case_df.date = pd.to_datetime(adm_case_df.date)

sgtf_df = pd.read_csv(ukhsa_omicron_sgtf_csv)
sgtf_df = sgtf_df[sgtf_df.sgtf == "Cases with SGTF"]
sgtf_df.drop(columns="sgtf", inplace=True)
sgtf_df.specimen_date = pd.to_datetime(sgtf_df.specimen_date, format="%d/%m/%Y")
sgtf_df.set_index("specimen_date", inplace=True)
sgtf_y_lab = "%OmicronSGTF"
sgtf_df.rename(columns={"percent": sgtf_y_lab}, inplace=True)

# No admissions figures in this dataset until 18 March 2020
march_18_2020 = dt(2020, 3, 18)
# No SGTF records in this dataset until 1 November 2021
november_1_2021 = dt(2021, 11, 1)

case_y_original = "newCasesBySpecimenDateRollingRate"
case_y_lab = case_y_original + "_%Dec2021Peak"
adm_y_original = "newAdmissionsRollingRate"
adm_y_lab = adm_y_original + "_%Jan2021Peak"
mort_y_original = "newDeaths28DaysByDeathDateRollingRate"
mort_y_lab = mort_y_original + "_%Jan2021Peak"
adm_case_df = adm_case_df[adm_case_df.date > march_18_2020]
adm_case_df.set_index("date", inplace=True)

peak_adm_jan_2021 = adm_case_df[adm_y_original].max()
adm_case_df[adm_y_lab] = 100 * adm_case_df[adm_y_original] / peak_adm_jan_2021

peak_case_dec_2021 = adm_case_df[case_y_original].max()
adm_case_df[case_y_lab] = 100 * adm_case_df[case_y_original] / peak_case_dec_2021

peak_mort_jan_2021 = adm_case_df[mort_y_original].max()
adm_case_df[mort_y_lab] = 100 * adm_case_df[mort_y_original] / peak_mort_jan_2021

sgtf_df = sgtf_df[sgtf_df.index > dt(2021,12,1)]

omi_case_df = adm_case_df[[case_y_lab]].join(sgtf_df[[sgtf_y_lab]]).dropna()
omi_y_lab = case_y_lab + "_OMICRON"
del_y_lab = case_y_lab + "_DELTA"
omi_case_df[omi_y_lab] = omi_case_df.prod(axis=1) / 100
omi_case_df[del_y_lab] = omi_case_df[case_y_lab] - omi_case_df[omi_y_lab]

adm_case_df = adm_case_df[adm_case_df.index > dt(2021,12,1)]

def main():
    plt.figure(figsize=(8, 8), dpi=250)
    adm_case_df[adm_y_lab].plot()
    adm_case_df[case_y_lab].plot(c="turquoise")
    omi_case_df[omi_y_lab].plot()
    omi_case_df[del_y_lab].plot()
    adm_case_df[mort_y_lab].plot()
    plt.tight_layout(pad=2)
    from_date = str(adm_case_df.index.min()).split(" ")[0]
    to_date = str(adm_case_df.index.max()).split(" ")[0]
    plt.xlabel(f"Date (from {from_date} to {to_date})")
    plt.ylabel("% of historic peak (cases/admissions) OR % of SGTF (Omicron)")
    plt.legend()
    plt.show()
    #plt.savefig("plots/rolling_cases_percentage_deaths_admissions_omicron_vs_delta_from_dec_2021.png")

#main()
