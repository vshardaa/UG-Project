%Uniform, Damped Soil layer on Rigid Bedrock
clc
clear

%obtain the full path of txt file
[filename1, pathname1]=uigetfile({'*.txt'},'file selector');
fullpathname1=strcat(pathname1,filename1);
text1=textread(fullpathname1);

%time: time vector in units of sec
time=text1(:,1);

%V: acceleration time history in units of g
V=text1(:,2);

%N: length of the signal V
N = length(V);

%Discrete Fourier transform
s=zeros(1,N);
for k=1:N
    for n=1:N
        s(k)=s(k)+V(n).*exp(-1i*2*pi*(k-1)*(n-1)/N);
    end
end

%freq: frequency vector in units of Hz
freq=linspace(0,25,N/2);
freq1=linspace(0,25,N);

%figure
subplot(5,1,1);
plot(time,V)
xlabel('\bfTime (sec)')
ylabel('\bfAcc. (g)')
title('\bfAcceleration time history of input earthquake')
grid on
xlim([0 time(end)])

ss=s(1:N/2);

subplot(5,1,2);
plot(freq,abs(ss))
xlabel('\bfFrequency (Hz)')
ylabel('\bfMag.')
title('\bfDiscrete Fourier transform of input earthquake')
grid on
xlim([0 freq(end)])

%Input values
H = 540; Vs = 1500; e = 0.05;

%to calculate transfer function
var1 = (2*pi*H)./Vs;
var2 = (cos(var1.*freq)).*(cos(var1.*freq));
var3 = (var1.*freq.*e).*(var1.*freq.*e);
var22 = (cos(var1.*freq1)).*(cos(var1.*freq1));
var33 = (var1.*freq1.*e).*(var1.*freq1.*e);

tfun = 1./sqrt(var2+var3);
tfun1 = 1./sqrt(var22+var33);

%figure
subplot(5,1,3);
plot(freq,abs(tfun))
xlabel('\bfFrequency (Hz)')
ylabel('\bf|F2|')
title('\bfTransfer function')
grid on
xlim([0 freq(end)])

%output fourier 
opval = ss.*tfun;
opval1 = s.*tfun1;

%figure
subplot(5,1,4);
plot(freq,abs(opval))
xlabel('\bfFrequency (Hz)')
ylabel('\bfMag.')
title('\bfDiscrete Fourier transform of output earthquake')
grid on
xlim([0 freq(end)])

%Inverse Discrete Fourier transform
s=opval1;
N = length(s);
sinv=zeros(1,N);
for n=1:N
    for k=1:N
        sinv(n)=sinv(n)+s(k).*exp(1i*2*pi*(k-1)*(n-1)/N);
    end
end
sinv=(1/N).*sinv;

subplot(5,1,5);
plot(time,real(sinv))
xlabel('\bfTime (sec)')
ylabel('\bfAcc. (g)')
title('\bfAcceleration time history of output earthquake')
grid on
xlim([0 time(end)])
