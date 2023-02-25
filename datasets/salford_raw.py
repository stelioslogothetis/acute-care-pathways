""" Constants for cleaner interaction with the original, raw dataset """

RawTimeseries = {
    "Blood_Haemoglobin": [
        "Haemoglobin_First",
        "Haemoglobin_24HPostAdm",
        "Haemoglobin_24HPreDsch",
        "Haemoglobin_Last",
    ],
    "Blood_Urea": [
        "Urea (serum)_First",
        "Urea (serum)_24HPostAdm",
        "Urea (serum)_24HPreDsch",
        "Urea (serum)_Last",
    ],
    "Blood_Sodium": [
        "Sodium (serum)_First",
        "Sodium (serum)_24HPostAdm",
        "Sodium (serum)_24HPreDsch",
        "Sodium (serum)_Last",
    ],
    "Blood_Potassium": [
        "Potassium (serum)_First",
        "Potassium (serum)_24HPostAdm",
        "Potassium (serum)_24HPreDsch",
        "Potassium (serum)_Last",
    ],
    "Blood_Creatinine": [
        "Creatinine_First",
        "Creatinine_24HPostAdm",
        "Creatinine_24HPreDsch",
        "Creatinine_Last",
    ],
    "Blood_DDimer": [
        "D-dimer_First",
        "D-dimer_24HPostAdm",
        "D-dimer_24HPreDsch",
        "D-dimer_Last",
    ],
    "Blood_CRP": [
        "C-Reactive protein_First",
        "C-Reactive protein_24HPostAdm",
        "C-Reactive protein_24HPreDsch",
        "C-Reactive protein_Last",
    ],
    "Blood_Albumin": [
        "Albumin_First",
        "Albumin_24HPostAdm",
        "Albumin_24HPreDsch",
        "Albumin_Last",
    ],
    "Blood_WhiteCount": ["WBC_First", "WBC_24HPostAdm", "WBC_24HPreDsch", "WBC_Last"],
    "VBG_Temperature": [
        "Temperature_Venous_First",
        "Temperature_Venous_24HPostAdm",
        "Temperature_Venous_24HPreDsch",
        "Temperature_Venous_Last",
    ],
    "VBG_pCO2": [
        "pCO2_Venous_First",
        "pCO2_Venous_24HPostAdm",
        "pCO2_Venous_24HPreDsch",
        "pCO2_Venous_Last",
    ],
    "VBG_pCO2_Corrected": [
        "pCO2_corrected_Venous_First",
        "pCO2_corrected_Venous_24HPostAdm",
        "pCO2_corrected_Venous_24HPreDsch",
        "pCO2_corrected_Venous_Last",
    ],
    "VBG_PH": [
        "PH_Venous_First",
        "PH_Venous_24HPostAdm",
        "PH_Venous_24HPreDsch",
        "PH_Venous_Last",
    ],
    "VBG_PH_Corrected": [
        "PH_corrected_Venous_First",
        "PH_corrected_Venous_24HPostAdm",
        "PH_corrected_Venous_24HPreDsch",
        "PH_corrected_Venous_Last",
    ],
    "VBG_O2": [
        "PO2_Venous_First",
        "PO2_Venous_24HPostAdm",
        "PO2_Venous_24HPreDsch",
        "PO2_Venous_Last",
    ],
    "VBG_O2_Corrected": [
        "PO2_corrected_Venous_First",
        "PO2_corrected_Venous_24HPostAdm",
        "PO2_corrected_Venous_24HPreDsch",
        "PO2_corrected_Venous_Last",
    ],
    "NEWS_Score": [
        "NEWS_score_first",
        "NEWS_score_24HPostAdm",
        "NEWS_score_24HPreDsch",
        "NEWS_score_Last",
    ],
    "NEWS_RespiratoryRate": [
        "NEWS_resprate_score_first",
        "NEWS_resprate_score_24HPostAdm",
        "NEWS_resprate_score_24HPreDsch",
        "NEWS_resprate_score_Last",
    ],
    "NEWS_BreathingDevice": [
        "NEWS_deviceair_score_first",
        "NEWS_deviceair_score_24HPostAdm",
        "NEWS_deviceair_score_24HPreDsch",
        "NEWS_deviceair_score_Last",
    ],
    "NEWS_O2Sat": [
        "NEWS_O2sat_score_first",
        "NEWS_O2sat_score_24HPostAdm",
        "NEWS_O2sat_score_24HPreDsch",
        "NEWS_O2sat_score_Last",
    ],
    "NEWS_Temperature": [
        "NEWS_temp_score_first",
        "NEWS_temp_score_24HPostAdm",
        "NEWS_temp_score_24HPreDsch",
        "NEWS_temp_score_Last",
    ],
    "NEWS_BP": [
        "NEWS_BP_score_first",
        "NEWS_BP_score_24HPostAdm",
        "NEWS_BP_score_24HPreDsch",
        "NEWS_BP_score_Last",
    ],
    "NEWS_HeartRate": [
        "NEWS_heartrate_score_first",
        "NEWS_heartrate_score_24HPostAdm",
        "NEWS_heartrate_score_24HPreDsch",
        "NEWS_heartrate_score_Last",
    ],
    "NEWS_AVCPU": [
        "NEWS_levelofcon_score_first",
        "NEWS_levelofcon_score_24HPostAdm",
        "NEWS_levelofcon_score_24HPreDsch",
        "NEWS_levelofcon_score_Last",
    ],
}

RawGroups = dict(
    Admin=["SpellSerial", "PatientNumber",],
    Spell=[
        "AdmissionDate",
        "TotalLOS",
        "LOSBand",
        "Outcode_Area",
        "DischargeDate",
        "CareHome",
        "Resus_Status",
    ],
    Demographics=["Gender", "Age", "Ethnicity",],
    AE=[
        "AE_PresentingComplaint",
        "AE_MainDiagnosis",
        "AE_Arrival",
        "AE_Departure",
        "AE_Location",
        "AE_PatientGroup",
        "AE_TriageNote",
    ],
    Text=[
        "AE_PresentingComplaint",
        "AE_MainDiagnosis",
        "AE_TriageNote",
        "MainDiagnosis",
        "MainProcedure",
    ],
    Admission=["AdmissionType", "AdmitMethod", "AdmissionSpecialty"],
    Discharge=[
        "DischargeConsultant",
        "DischargeSpecialty",
        "DischargeDestination",
        "DiedDuringStay",
        "DiedWithin30Days",
    ],
    Wards=["AdmitWard"] + [f"NextWard{_}" for _ in range(2, 10)] + ["DischargeWard"],
    WardLOS=["AdmitWardLoS"]
    + [f"NextWardLOS{_}" for _ in range(2, 10)]
    + ["DischargeWardLOS"],
    ICD10=["MainICD10"] + [f"SecDiag{_}" for _ in range(1, 16)],
    OPCS4=["MainOPCS4"] + [f"SecOper{_}" for _ in range(1, 15)],
    Blood=[
        col for col, parent in RawTimeseries.items() if str(parent).startswith("Blood_")
    ],
    VBG=[
        col for col, parent in RawTimeseries.items() if str(parent).startswith("VBG_")
    ],
    NEWS=[
        col for col, parent in RawTimeseries.items() if str(parent).startswith("NEWS_")
    ],
    CompositeScores=["CFS_score", "Waterlow_Score", "Waterlow_Outcome"],
)

_timeseries_labelling = ['Admission', '24HPostAdm', '24HPreDisch', 'Discharge']
SalfordTimeseries = {
    parent: [f'{parent}_{_timeseries_labelling[_]}' for _ in range(len(cols))] for parent, cols in RawTimeseries.items()
}

RedundantColumns = [
    'PatientType', # Every value is "Inpatients"
    'CCG', # Hospital is probably unimportant
    'AdmissionConsultant',
    'Over7Days',
    'Over14Days',
    'GP_Practice',
    'SpellCount', # Every value is 1
] + [
    'AdmitWardEnd', 'CFS_recorded_dtm', 'Waterlow_recorded_dtm', 'Status_recorded_dtm', 'HaemFirst_recorded_dtm', 'Haem24HPostAdm_recorded_dtm', 'Haem24HPreDsch_recorded_dtm', 'HaemLast_recorded_dtm', 'UreaFirst_recorded_dtm', 'Urea24HPostAdm_recorded_dtm', 'Urea24HPreDsch_recorded_dtm', 'UreaLast_recorded_dtm', 'SodiumFirst_recorded_dtm', 'Sodium24HPostAdm_recorded_dtm', 'Sodium24HPreDsch_recorded_dtm', 'SodiumLast_recorded_dtm', 'PotassiumFirst_recorded_dtm', 'Potassium24HPostAdm_recorded_dtm', 'Potassium24HPreDsch_recorded_dtm', 'PotassiumLast_recorded_dtm', 'CreatinineFirst_recorded_dtm', 'Creatinine24HPostAdm_recorded_dtm', 'Creatinine24HPreDsch_recorded_dtm','CreatinineLast_recorded_dtm','D-dimerFirst_recorded_dtm', 'D-dimer24HPostAdm_recorded_dtm', 'D-dimer24HPreDsch_recorded_dtm', 'D-dimerLast_recorded_dtm', 'CRPFirst_recorded_dtm', 'CRP24HPostAdm_recorded_dtm', 'CRP24HPreDsch_recorded_dtm', 'CRPLast_recorded_dtm', 'AlbuminFirst_recorded_dtm', 'Albumin24HPostAdm_recorded_dtm', 'Albumin24HPreDsch_recorded_dtm', 'AlbuminLast_recorded_dtm', 'WBCFirst_recorded_dtm', 'WBC24HPostAdm_recorded_dtm', 'WBC24HPreDsch_recorded_dtm', 'WBCLast_recorded_dtm', 'TempVenousFirst_recorded_dtm', 'TempVenous24HPostAdm_recorded_dtm', 'TempVenous24HPreDsch_recorded_dtm', 'TempVenousLast_recorded_dtm', 'pCO2VenousFirst_recorded_dtm', 'pCO2Venous24HPostAdm_recorded_dtm', 'pCO2Venous24HPreDsch_recorded_dtm', 'pCO2VenousLast_recorded_dtm', 'pCO2correctedFirst_recorded_dtm', 'pCO2corrected24HPostAdm_recorded_dtm', 'pCO2corrected24HPreDsch_recorded_dtm', 'pCO2correctedLast_recorded_dtm', 'PHFirst_recorded_dtm', 'PH24HPostAdm_recorded_dtm', 'PH24HPreDsch_recorded_dtm','PHLast_recorded_dtm', 'PHcorrectedFirst_recorded_dtm', 'PHcorrected24HPostAdm_recorded_dtm', 'PHcorrected24HPreDsch_recorded_dtm', 'PHcorrectedLast_recorded_dtm', 'PO2First_recorded_dtm', 'PO2_24HPostAdm_recorded_dtm', 'PO2_24HPreDsch_recorded_dtm', 'PO2Last_recorded_dtm', 'PO2correctedFirst_recorded_dtm', 'PO2corrected24HPostAdm_recorded_dtm', 'PO2corrected24HPreDsch_recorded_dtm', 'PO2correctedLast_recorded_dtm', 'NEWS_First_recorded_dtm', 'NEWS_24HPostAdm_recorded_dtm', 'NEWS_24HPreDsch_recorded_dtm', 'NEWS_Last_recorded_dtm', 
]

AEDiagnosisStems = [
    "confus",
    "weak",
    "found",
    "fof",
    "dementia",
    "discharged",
    "sob",
    "unwitnessed",
    "gcs",
    "diarrh",
    "vomit",
    "collaps",
    "sudden",
    "woke",
    "dizz",
    "tight",
    "head",
    "fall",
    "fell",
    "pain",
    "bang",
    "mobility",
    "cope",
    "coping",
    "weak",
    "deterio",
]

AEVaguePresentingComplaints = [
    "referral to service (procedure)",
    "generally unwell (finding)",
    "unwell adult",
    "unknown",
    "other",
    "general deterioration",
    "generally unwell",
    "gen unwell",
]