cat ~/.ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDzQLfAglFa/FppWzdMg3rugW9vUdoq0Dfp8RslDUvN+M5fc9tgMSactm2R6H9LZ2WRJSIhEhZaEdbREjep0La8kygVTha/wRW3hf+XpIPu0yFm7+gl0POdeXqzJM/HlNEmQ+sKb4g4Rye8VNICLJqksjJ5NN7mXsfAjJNdo9skK3BNGJAFfu84X91QoV/lqqiSQrBI3VOFD6lxRuNAXBf+j3boWHLoPJEs38oEbxt+RXrTcLPXtEcoDBBbUjtYWSNgvCto+HrGdFUOZRenxGBBw6h2qJ0cgbw567dbLVtNbdRMInCGmrCOi4rJMbOHrFf2UW0V9rc3LzhtyD/DgR/T ubuntu@ip-172-31-39-205
ubuntu@ip-172-31-39-205:~/git$ git pull git@github.com:sekharr606/bittu.git
The authenticity of host 'github.com (13.234.176.102)' can't be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,13.234.176.102' (ECDSA) to the list of known hosts.
fatal: Couldn't find remote ref HEAD
ubuntu@ip-172-31-39-205:~/git$ git remote add origin git@github.com:sekharr606/bittu.git
ubuntu@ip-172-31-39-205:~/git$ git branch -M main
ubuntu@ip-172-31-39-205:~/git$ git push -u origin main
Warning: Permanently added the ECDSA host key for IP address '13.234.210.38' to the list of known hosts.
Counting objects: 6, done.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 470 bytes | 470.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To github.com:sekharr606/bittu.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin
