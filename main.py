import barrel_GCode
import plunger_GCode

def fileCreate(coreFileName, cavityFileName, plungerFileName, g_code1, g_code2, g_code3):
    syringeCoreFile = open(coreFileName, "w+")
    syringeCoreFile.write(g_code1)
    syringeCoreFile.close()

    syringeCavityFile = open(cavityFileName, "w+")
    syringeCavityFile.write(g_code2)
    syringeCavityFile.close()

    plungerMoldFile =open(plungerFileName, "w+")
    plungerMoldFile.write(g_code3)
    plungerMoldFile.close()

    print("Success! NC files saved in ./CNC_code_py")

print("""Syringe mold CNC Program generator\n
        [1] 0.5ml
        [2] 1.0ml
        [3] 1.5ml
        [4] 2.25ml
        [5] 3.0ml
        [6] 5.0ml
        [7] 10.0ml
        [8] 20.0ml\n""")

while True:
    syringe_capacity = float(input("Enter desired syringe capacity from the given options: "))

    if syringe_capacity == 0.5:
        print("Still working on it.")
        break
    elif syringe_capacity == 1.0:
        fileCreate("1ml_barrelCore.NC", "1ml_barrelCavity.NC", "1ml_plunger.NC", barrel_GCode.one_ml_core, barrel_GCode.one_ml_cavity, plunger_GCode.one_ml_mold)
        break
    elif syringe_capacity == 1.5:
        fileCreate("1_5ml_barrelCore.NC", "1_5ml_barrelCavity.NC", "1_5ml_plunger.NC", barrel_GCode.oneAndHalf_ml_core, barrel_GCode.oneAndHalf_ml_cavity, plunger_GCode.oneAndHalf_ml_mold)
        break
    elif syringe_capacity == 2.25:
        fileCreate("2_25ml_barrelCore.NC", "2_25ml_barrelCavity.NC", "2_25ml_plunger.NC", barrel_GCode.twoAndQuarter_ml_core, barrel_GCode.twoAndQuarter_ml_cavity, plunger_GCode.twoAndQuarter_ml_mold)
        break
    elif syringe_capacity == 3.0:
        fileCreate("3ml_barrelCore.NC", "3ml_barrelCavity.NC", "3ml_plunger.NC", barrel_GCode.three_ml_core, barrel_GCode.three_ml_cavity, plunger_GCode.three_ml_mold)
        break
    elif syringe_capacity == 5.0:
        fileCreate("5ml_barrelCore.NC", "5ml_barrelCavity.NC", "5ml_plunger.NC", barrel_GCode.five_ml_core, barrel_GCode.five_ml_cavity, plunger_GCode.five_ml_mold)
        break
    elif syringe_capacity == 10.0:
        fileCreate("10ml_barrelCore.NC", "10ml_barrelCavity.NC", "10ml_plunger.NC", barrel_GCode.ten_ml_core, barrel_GCode.ten_ml_cavity, plunger_GCode.ten_ml_mold)
        break
    elif syringe_capacity == 20.0:
        fileCreate("20ml_barrelCore.NC", "20ml_barrelCavity.NC", "20ml_plunger.NC", barrel_GCode.twenty_ml_core, barrel_GCode.twenty_ml_cavity, plunger_GCode.twenty_ml_mold)
        break
    else:
        print("\nInvalid choice. Try again")