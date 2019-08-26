function [J, grad] = costFunction(theta, X, y)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
theta_length = length(theta);
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%
for i = 1:m
    sigmoid_of_x = sigmoid(X(i,:) * theta);
    J += -(y(i)) * log(sigmoid_of_x) - (1 - y(i)) * log(1 - sigmoid_of_x);
endfor
J /= m;

for j = 1:theta_length
    curr_grad = 0;
    for i = 1:m
        sigmoid_of_x = sigmoid(X(i,:) * theta);
        curr_grad += (sigmoid_of_x - y(i)) * X(i,j);
    endfor
    grad(j) = curr_grad / m;
endfor


% =============================================================

end
