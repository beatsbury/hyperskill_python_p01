spin = input()
charge = input()

if charge == "0":
    print("Photon Boson" if spin == "1" else "Neutrino Lepton")
elif charge == "-1/3":
    print("Strange Quark")
elif charge == "2/3":
    print("Charm Quark")
elif charge == "-1":
    print("Electron Lepton")
else:
    print("Wrong input")
