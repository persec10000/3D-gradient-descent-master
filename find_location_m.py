[X, Y] = (mslice[-2:.5:10])
Rx = mcat([0.1, 2.7, 7.1, 9.1, 0.1, 0.1, 9.9, 0.9])
Ry = mcat([2.1, 9.1, 1.2, 8.7, 0.1, 9.9, 0.1, 9.9])
w = mcat([1.4, 1.8, 1.6, 1.5, 9, 9, 9, 9])
C = mcat([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
r = mcat([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
R = sqrt(X **elpow** 2 + Y **elpow** 2) + eps
Z = 0 * sin(R)

for k in mslice[1:length(X)]:
    for j in mslice[1:length(Y)]:
        for i in mslice[1:length(Rx)]:
            d = sqrt((X(k, j) - Rx(i)) ** 2 + (Y(k, j) - Ry(i)) ** 2) / 15.1
            d = sqrt((X(k, j) - Rx(i)) ** 2 + (Y(k, j) - Ry(i)) ** 2) / 1.1
            C(i).lvalue = d + w(i) * (exp(d) / (1 + exp(d))) * r(i)
            Z(k, j).lvalue = Z(k, j) + C(i)
        end

    end

end


figure()


surf(X, Y, Z, mstring('FaceAlpha'), 0.5)