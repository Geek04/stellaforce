from argparse import ArgumentParser

from cryptography.fernet import Fernet

from stellaforce.encryption import JSONFernetEncryptor


def main():
    parser = ArgumentParser(prog=__name__, description="Encrypt and valideate JSON using various encryption types.")
    parser.add_argument("--key", help="Private key for data to be encrypted.", required=True)
    parser.add_argument("--etype", help="Type of encryption to be used. Supported types: Fernet. Default: Fernet",
                        default="Fernet")
    parser.add_argument("--ftype", help="Type of file type. Supported types: JSON. Default: JSON", default="JSON")
    parser.add_argument("--verbose", help="If added, prints out encrypted data", default=False)
    parser.add_argument("path",
                        help="Path to JSON file to be encrypted.",
                        metavar="P", type=str)

    args = parser.parse_args()

    key = args.key
    file_path = args.path
    verbose = args.verbose

    fernet_instance = Fernet(key)
    encryptor = JSONFernetEncryptor(fernet_instance)
    encrypted_data = encryptor.encrypt(file_path)

    if verbose:
        print(encrypted_data)


if __name__ == "__main__":
    main()