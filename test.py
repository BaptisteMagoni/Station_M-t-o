def byte_afficherBytearrayHexa(self, tableOctet, separateur=' '):
    for idx, octet in enumerate(tableOctet):
        if idx != len(tableOctet) - 1:
            print("%s%s" % ('{:02x}'.format(octet), separateur), end='')
        else:  # évite d'afficher le séparateur après le dernier octet affiché
            print('{:02x}'.format(octet))