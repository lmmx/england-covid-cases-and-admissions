import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt

ukhsa_national_case_csv = "data/ukhsa_national_covid_case_rolling_rates_and_admissions.csv"
ukhsa_omicron_sgtf_csv = "data/ukhsa_sgtf_totalepicurve_2021-12-20-1.csv"

adm_case_df = pd.read_csv(ukhsa_national_case_csv)
adm_case_df.date = pd.to_datetime(adm_case_df.date)
adm_case_df = adm_case_df[adm_case_df.date > dt(2021,6,1)]

sgtf_df = pd.read_csv(ukhsa_omicron_sgtf_csv)
sgtf_df = sgtf_df[sgtf_df.sgtf == "Cases with SGTF"]
sgtf_df.drop(columns="sgtf", inplace=True)
sgtf_df.specimen_date = pd.to_datetime(sgtf_df.specimen_date, format="%d/%m/%Y")
sgtf_df.set_index("specimen_date", inplace=True)
sgtf_y_lab = "percentOmicronSGTF"
sgtf_df.rename(columns={"percent": sgtf_y_lab}, inplace=True)

# No admissions figures in this dataset until 18 March 2020
march_18_2020 = dt(2020, 3, 18)
# No SGTF records in this dataset until 1 November 2021
november_1_2021 = dt(2021, 11, 1)

case_y_original = "newCasesBySpecimenDateRollingRate"
case_y_lab = "newCasesBySpecimenDateRollingRatePercentageDec2021Peak"
adm_y_original = "newAdmissions"
adm_y_lab = "newAdmissionsPercentageJan2021Peak"
adm_case_df = adm_case_df[adm_case_df.date > march_18_2020]
adm_case_df.set_index("date", inplace=True)

peak_adm_jan_2021 = adm_case_df[adm_y_original].max()
adm_case_df[adm_y_lab] = 100 * adm_case_df[adm_y_original] / peak_adm_jan_2021

peak_case_dec_2021 = adm_case_df[case_y_original].max()
adm_case_df[case_y_lab] = 100 * adm_case_df[case_y_original] / peak_case_dec_2021

omi_case_df = adm_case_df[[case_y_lab]].join(sgtf_df[[sgtf_y_lab]]).dropna()
omi_y_lab = "newCasesOmicronRollingRatePercentageDec2021TotalPeak"
del_y_lab = "newCasesDeltaRollingRatePercentageDec2021TotalPeak"
omi_case_df[omi_y_lab] = omi_case_df.prod(axis=1) / 100
omi_case_df[del_y_lab] = omi_case_df[case_y_lab] - omi_case_df[omi_y_lab]

def main():
    plt.figure(figsize=(16, 8), dpi=250)
    adm_case_df[case_y_lab].plot()
    adm_case_df[adm_y_lab].plot()
    omi_case_df[omi_y_lab].plot()
    omi_case_df[del_y_lab].plot()
    plt.tight_layout(pad=2)
    from_date = str(adm_case_df.index.min()).split(" ")[0]
    to_date = str(adm_case_df.index.max()).split(" ")[0]
    plt.xlabel(f"Date (from {from_date} to {to_date})")
    plt.ylabel("% of historic peak (cases/admissions) OR % of SGTF (Omicron)")
    plt.legend()
    plt.show()
    #plt.savefig("plots/rolling_cases_percentage_and_admissions_omicron_vs_delta_6_months.png")

#main()
