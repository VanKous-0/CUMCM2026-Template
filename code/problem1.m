% Problem 1 Matlab placeholder.
% Replace the sample data and method with the team's complete implementation.
data = [8, 6, 7; 7, 9, 6; 6, 7, 9];
weights = [0.40; 0.35; 0.25];
normalized = normalize(data, 'range');
scores = normalized * weights;
disp(scores);
