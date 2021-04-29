# sanna

<br/>#Task name: GitHub
<br/>##Task preparation: <br/>
1/ install Ubuntu in VirtualBox<br/>
2/ install git on Ubuntu<br/>
3/ connect Ubuntu terminal to GitHub<br/>
##Task implementation:<br/>
1/Open terminal<br/>
2/Execute: sudo apt-get install git<br/>
3/Execute: sudo mkdir Devasc_Skills<br/>
4/Execute: vi README.MD<br/>
5/Execute: git init<br/>
6/Execute: git add README.md <br/>
7/Execute: git commit -m "initial"<br/>
8/Execute: git branch -M main<br/>
9/Execute: git remote add origin https://github.com/sanna986/sanna986.git<br/>
10/Execute: git push -u origin main<br/>
Task troubleshooting:<br/>
1/ No Internet on Virtualbox<br/>
2/ Forgot password of my GitHub account<br/>
3/ Git was not installed on Ubuntu<br/>
Task Verification:<br/>
The README.MD file was added to the repository: https://github.com/sanna986/sanna986<br/>



<br/>#Task name: Ansible
<br/>##Task preparation: <br/>
1/ Create VirtualBox CSR1000V<br/>
2/ Connect DEVASC LAB VM with CSR1000V<br/>
##Task implementation:<br/>
1/Create host file <br/>
2/Create config file to link to correct host file<br/>
3/ Create and develop yml file to run Ansible code<br/>
Task troubleshooting:<br/>
1/ Had issues with the CSR1000v setup: I did not strictly follow the lab doc.<br/>
So there was no interface setup... I did it manually but then SSH refused connection.<br/>
Task Verification:<br/>
The Ansible script runs and gives the same output as i would run on router<br/>


<br/>#Task name: RESTCONF
<br/>##Task preparation: <br/>
1/ Setup Restconf in CSR1000V<br/>
##Task implementation:<br/>
1/add ip + port + username + password in the urls <br/>
2/change curl command to python requests.post(...) with the parameters<br/>
<br/>
Task troubleshooting:<br/>
I copied the urls and changed them but because of a weird character that was pasted i got errors<br/>
