%% a,c
clc
clear
clf

t = (1:300);
alpha = 0.01;
eta_0 = 900;
R=(1:0.1:30);
matrix = zeros(length(R), 100);

for i = 1:length(R)
    current = eta_0;
    for j=1:length(t)
        next = R(i)*current*exp(-alpha*current);
        if j > 200
            matrix(i,j-200) = next;
        end
        current = next;
    end
end
scatter(R, matrix, 1, 'filled', 'k')
%% b
clc
clear
clf

t = (1:41);
alpha = 0.01;
eta_0 = 900;
R=[5, 10, 22.9, 13.5]
% [1, 7] 1 FP
% [8, 12] 2 Point Cycle
% [22.5, 23.4] 3 Point Cycle
% [13, 14] 4 Point Cycle
matrix = zeros(length(R), 41);

for i = 1:length(R)
    current = eta_0;
    matrix(i,1) = current;
    for j=2:length(t)
        next = R(i)*current*exp(-alpha*current);
        matrix(i,j) = next;
        current = next;
    end
    subplot(2,2,i)
    plot(t, matrix(i,:), '-s')
    title(sprintf('R=%.1f',R(i)))
    ylabel('\eta')
    xlabel('\tau')
end
%% d
clc
clear
clf

t = (1:41);
alpha = 0.01;
eta_0 = 900;
R=[14.7, 14.8, 14.9, 16]
matrix = zeros(length(R), 41);

for i = 1:length(R)
    current = eta_0;
    matrix(i,1) = current;
    for j=2:length(t)
        next = R(i)*current*exp(-alpha*current);
        matrix(i,j) = next;
        current = next;
    end
    subplot(2,2,i)
    plot(t, matrix(i,:), '-s')
    title(sprintf('R=%.1f',R(i)))
end