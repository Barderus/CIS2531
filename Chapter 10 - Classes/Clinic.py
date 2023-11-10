'''
Next, write a program that creates an instance of the Patient class, initialized with sample data. 
Then, create three instances of the Procedure class, initialized with the following data:
Procedure #1:                     Procedure #2:                 Procedure #3:
Procedure name: Physical Exam     Procedure name: X-ray         Procedure name: Blood test
Date: Today’s date                Date: Today’s date            Date: Today’s date
Practitioner: Dr. Irvine          Practitioner: Dr. Jamison     Practitioner: Dr. Smith
Charge: 250.00                    Charge: 500.00                Charge: 200.00

'''
import Procedure as pr
import Patient as pa
def main():
    procedure1 = pr.Procedure("Physical Exam", "11/8/2023","Dr. Irvine", 250.00)
    procedure2 = pr.Procedure("X-ray", "11/8/2023", "Dr. Jamison", 500.00)
    procedure3 = pr.Procedure("Blood Test", "11/8/2023", "Dr. Smith", 200.00)
    
    patient1 = pa.Patient("Henry", "Matthew", "Waterman","118 E 3rd St", "Hinsdale",              "IL", "60521", "214-824-0329", "Matthew Waterman", "214-923-0328")
    patient2 = pa.Patient("Gabriel", "Felipe", "dos Reis", "Gilberto Batista de Souza, 70", "Aracatuba",              "SP", "16012-525", "469-649-6982", "Ellen Santos", "1234-5678")
    patient3 = pa.Patient("Fiona", "Elizabeth", "Carruth", "123 Harvard St", "Elmhurst",
                  "IL", "60439", "098-765-4321", "Gabriel Carruth", "468-648-6882")
    
    patient_dct = {patient1:procedure1, patient2:procedure2, patient3:procedure3}
    
    for patient, procedure in patient_dct.items():
        print(f"Patient Information:\n{patient}")
        print()
        print(f"Procedure Information:\n{procedure}")
        print()
    
main()