# author: Xinhai Zou
# Copyright Xinhai Zou

################################################
#
# Import packages
#
################################################
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import argparse

################################################
#
# Core function
#
################################################
def build_key(username, password):
    keyPair = RSA.generate(3072)
    # generate public key
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey(passphrase=password)
    # generate private key
    privKeyPEM = keyPair.exportKey(passphrase=password)
    
    # output public key file
    f1 = open('%s.public' % (username), 'wb')
    f1.write(pubKeyPEM)
    f1.close()
    
    # output private key file
    f2 = open('%s.private' % (username), 'wb')
    f2.write(privKeyPEM)
    f2.close()
    
    
def encrypt(public_key_path, filename, password, message):
    # load public key
    f1 = open(public_key_path, 'rb')
    key = RSA.import_key(f1.read(), passphrase=password)
    
    # encrypt password
    encryptor = PKCS1_OAEP.new(key)
    encrypted = encryptor.encrypt(message.encode('ascii'))
    
    # output private key file
    f2 = open('%s.rsa' % (filename), 'wb')
    f2.write(encrypted)
    f2.close()
    
    
def decrypt(private_key_path, filename, password):
    # load private key
    f1 = open(private_key_path, 'rb')
    key = RSA.import_key(f1.read(), passphrase=password)
    
    # load encrypted file
    f2 = open('%s.rsa' % (filename), 'rb')
    encrypted = f2.read()
    
    # decrypt password
    decryptor = PKCS1_OAEP.new(key)
    decryp_mes = decryptor.decrypt(encrypted)
    
    return decryp_mes


################################################
#
# For terminal
#
################################################
def blue_str(line):
    return ('\033[1;34m' + line + '\033[0m')


def green_str(line):
    return ('\033[1;32m' + line + '\033[0m')


def red_str(line):
    return ('\033[1;31m' + line + '\033[0m')


def parse_arguments():
    tasks = ['build_keys', 'encrypt', 'decrypt']
    parser = argparse.ArgumentParser(
    description = 'Tool for encrypt and decrypt messages by RSA. \
        \n\t1. Build Keys: you should fill in the "-u" and "-p" \
        \n\t2. Encrypt Messages: you should fill in the "-pub", "f", "p" and "m" \
        \n\t3. Decrypt Messages: you should fill in the "-pri", "f" and "p"      \
        \nFor more details, see "-p" \
        ')
    parser.add_argument('--task', choices=tasks)
    parser.add_argument('-u', type=str, help='name for built public key and private key', default='')
    parser.add_argument('-p', type=str, help='password to log in public key and private key', default='')
    parser.add_argument('-pub', type=str, help='public key path', default='')
    parser.add_argument('-pri', type=str, help='private key path', default='')
    parser.add_argument('-f', type=str, help='file name for encrypted file', default='')
    parser.add_argument('-m', type=str, help='plaintext message', default='')
    args = parser.parse_args()
    
    return args


if __name__ == '__main__':
    args = parse_arguments()
    task = args.task

    username, password, public_key_path, private_key_path, filename, message = \
    args.u, args.p, args.pub, args.pri, args.f, args.m
    
    if task == 'build_keys':
        print(blue_str('BUILD KEYS TASK'))
        if username == '' or password == '':
            print(red_str('ERROR: username or password cannot be empty!'))
        else:
            build_key(username, password)
            print(green_str('SUCCESS: %s.public and %s.private has been generated in the current directory.' % (username, username)))

    elif task == 'encrypt':
        print(blue_str('ENCRYPT THE MESSAGE TASK'))
        if public_key_path == '' or filename == '' or password == '' or message == '':
            print(red_str('ERROR: public key path or filename or password or message cannot be empty!'))
        else:
            encrypt(public_key_path, filename, password, message)
            print(green_str('SUCCESS: %s.rsa has been built in the current directory' % (filename)))

    elif task == 'decrypt':
        print(blue_str('DECRYPT THE MASSAGE TASK'))
        if private_key_path == '' or filename == '' or password == '':
            print(red_str('ERROR: private key path or filename or password cannot be empty!'))
        else:
            decryp_mes = decrypt(private_key_path, filename, password)
            print(green_str('SUCCESS: the decrypted message is %s' % (decryp_mes)))

    else:
        print(red_str('INVALID TASK %s' % (task)))