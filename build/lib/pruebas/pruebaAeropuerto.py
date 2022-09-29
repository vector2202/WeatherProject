from src import aeropuerto

def main():
    aeropuertoPrueba = aeropuerto.Aeropuerto('MEX', 10, 100)
    assert(aeropuertoPrueba.funcionHash(11) == 3)

main()
