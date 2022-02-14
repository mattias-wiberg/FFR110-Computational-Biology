clf
clc
clear

r = 0.1;
K = 10^3;
b = 1;
t = [2:100];
N0 = [1,2,3,10];
for j = 1:length(N0)
    points = [N0(j)];
    approx = [N0(j)];
    for i=t
        points = [points (r+1)*points(i-1)/(1+(points(i-1)/K)^b)];
        approx = [approx (r+1)*approx(i-1)];
    end
    subplot(2,2,j)
    loglog([1 t],points);
    hold on
    loglog([1 t],approx);
    legend('real', 'approx');
    ylabel('Number of Induviduals')
    xlabel('Generation [\tau]')
    title(sprintf("N_0= %.0f",N0(j)))
end
%% F
clf
clc
clear

r = 0.1;
K = 10^3;
b = 1;
t = [2:100];
N0 = -1*[1,2,3,10];
for j = 1:length(N0)
    points = [K*r^(1/b)+N0(j)];
    approx = [N0(j)];
    for i=t
        points = [points (r+1)*points(i-1)/(1+(points(i-1)/K)^b)];
        approx = [approx (1-(b*r/(r+1)))*approx(i-1)];
    end
    subplot(2,2,j)
    plot([1 t],points);
    
    hold on
    plot([1 t],approx+K*r^(1/b));
    legend('real', 'approx');
    ylabel('Number of Induviduals')
    xlabel('Generation [\tau]')
    title(sprintf("N_0= %.0f",N0(j)))
end