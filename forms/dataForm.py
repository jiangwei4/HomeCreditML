from django import forms



ORGANIZATION_TYPE_CHOICES = [
    ('Business Entity Type 3', 'Business Entity Type 3'), ('School', 'School'), ('Government', 'Government'), ('Religion', 'Religion'),
    ('Other', 'Other'), ('XNA', 'XNA'), ('Electricity', 'Electricity'), ('Medicine', 'Medicine'), ('Business Entity Type 2', 'Business Entity Type 2' ), ('Self-employed', 'Self-employed'), ('Transport: type 2', 'Transport: type 2'), ('Construction', 'Construction'), ('Housing', 'Housing'), ('Kindergarten', 'Kindergarten'), ('Trade: type 7', 'Trade: type 7'), ('Industry: type 11', 'Industry: type 11'), ('Military', 'Military'), ('Services', 'Services'), ('Security Ministries', 'Security Ministries'), ('Transport: type 4', 'Transport: type 4'), ('Industry: type 1', 'Industry: type 1'), ('Emergency', 'Emergency'), ('Security', 'Security'), ('Trade: type 2', 'Trade: type 2'), ('University', 'University'), ('Transport: type 3' , 'Transport: type 3' ), ('Police', 'Police'), ('Business Entity Type 1', 'Business Entity Type 1'), ('Postal', 'Postal'), ('Industry: type 4', 'Industry: type 4'), ('Agriculture', 'Agriculture'), ('Restaurant', 'Restaurant'), ('Culture', 'Culture'), ('Hotel', 'Hotel'), ('Industry: type 7', 'Industry: type 7'), ('Trade: type 3', 'Trade: type 3'), ('Industry: type 3', 'Industry: type 3'), ('Bank', 'Bank'), ('Industry: type 9', 'Industry: type 9'), ('Insurance', 'Insurance'), ('Trade: type 6', 'Trade: type 6'), ('Industry: type 2', 'Industry: type 2'), ('Transport: type 1', 'Transport: type 1'), ('Industry: type 12', 'Industry: type 12'), ('Mobile', 'Mobile'), ('Trade: type 1' , 'Trade: type 1'), ('Industry: type 5', 'Industry: type 5'), ('Industry: type 10', 'Industry: type 10'), ('Legal Services', 'Legal Services'), ('Advertising', 'Advertising'), ('Trade: type 5', 'Trade: type 5'), ('Cleaning', 'Cleaning'), ('Industry: type 13', 'Industry: type 13'), ('Trade: type 4', 'Trade: type 4'), ('Telecom', 'Telecom'), ('Industry: type 8', 'Industry: type 8'), ('Realtor', 'Realtor'), ('Industry: type 6' 'Industry: type 6')
]

NAME_FAMILY_STATUS_CHOICES = [
    ('Single / not married', 'Single / not married'), ('Married', 'Married'), ('Civil marriage', 'Civil marriage')
]

WALLSMATERIAL_MODE_CHOICES = [
    ('Stone, brick', 'Stone, brick'), ('Panel', 'Panel'), ('Mixed', 'Mixed'), ('Others', 'Others'), ('Block', 'Block'), ('Monolithic', 'Monolithic')
]

WEEKDAY_APPR_PROCESS_START_CHOICES = [
    ('MONDAY', 'Lundi'), ('TUESDAY', 'Mardi'), ('WEDNESDAY', 'Mercredi'), ('THURSDAY', 'Jeudi'), ('FRIDAY', 'Vendredi'), ('SATURDAY', 'Samedi'), ('SUNDAY', 'Dimanche')
]

CODE_GENDER_CHOICES = [
    ('M', 'M'), ('F', 'F')
]

NAME_CONTRACT_TYPE_CHOICES = [
    ('Revolving loans', 'Revolving loans'), ('Cash loans', 'Cash loans')
]

NAME_TYPE_SUITE_CHOICES = [
    ('Unaccompanied', 'Unaccompanied'), ('Family', 'Family'), ('Children', 'Children'), ('Spouse, partner', 'Spouse, partner')
]


class DataForm(forms.Form):
    #ORGANIZATION_TYPE = forms.ChoiceField(label="Type d'organisation", choices=ORGANIZATION_TYPE_CHOICES)    
    ELEVATORS_AVG = forms.FloatField(label="Nombre moyen d'ascenseurs")    
    NAME_FAMILY_STATUS = forms.ChoiceField(label="Situation marital", choices=NAME_FAMILY_STATUS_CHOICES)    
    WALLSMATERIAL_MODE = forms.ChoiceField(label="Materiaux du domicile", choices=WALLSMATERIAL_MODE_CHOICES)    
    FLAG_DOCUMENT_5 = forms.BooleanField()    
    #OCCUPATION_TYPE = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")    
    FLAG_OWN_CAR = forms.BooleanField(label="Possède une voiture")    
    YEARS_BEGINEXPLUATATION_AV = forms.FloatField()    
    FLAG_DOCUMENT_17 = forms.BooleanField()    
    WEEKDAY_APPR_PROCESS_START = forms.ChoiceField(help_text="Jour de lancement du processus", choices=WEEKDAY_APPR_PROCESS_START_CHOICES)    
    LIVINGAREA_AVG = forms.FloatField()    
    NONLIVINGAREA_AVG = forms.FloatField()   
    DAYS_ID_PUBLISH = forms.IntegerField()    
    REGION_POPULATION_RELATIVE = forms.FloatField()    
    FLAG_OWN_REALTY = forms.BooleanField()    
    APARTMENTS_MODE = forms.FloatField()    
    FONDKAPREMONT_MODE = forms.FloatField()    
    CODE_GENDER = forms.ChoiceField(label="Sex", choices=CODE_GENDER_CHOICES)    
    BASEMENTAREA_MODE = forms.FloatField()    
    NAME_CONTRACT_TYPE = forms.ChoiceField(label="Type de contrat", choices=NAME_CONTRACT_TYPE_CHOICES)    
    HOUSETYPE_MODE = forms.FloatField()
    FLOORSMAX_MODE = forms.FloatField()
    LANDAREA_AVG = forms.FloatField()
    LIVINGAPARTMENTS_AVG = forms.FloatField()
    EXT_SOURCE_1 = forms.FloatField()
    EXT_SOURCE_2 = forms.FloatField()
    EXT_SOURCE_3 = forms.FloatField()
    TARGET = forms.BooleanField()
    NAME_TYPE_SUITE = forms.ChoiceField(choices=NAME_TYPE_SUITE_CHOICES)

