function g = sigmoid(z)
%SIGMOID Compute sigmoid function
%   g = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
 g = zeros(size(z));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).

dims = size(z);
for rows = 1:dims(1)
    for cols = 1:dims(2)
        curr_z = z(rows,cols);
        g(rows,cols) = 1/(1+exp(-curr_z));
    endfor
endfor

% =============================================================

end
