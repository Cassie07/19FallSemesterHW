% Please edit this function only, and submit this Matlab file in a zip file
% along with your PDF report

function [r,c] = i_spy (object_im, big_im)
n1 = 0.59422;
n2 = 0.26;
n3 = 0.3148;
%object_im = Object image that needs to be detected
%big_im = Image in which detections needs to be done.
Rp = size(big_im, 1);
Cp = size(big_im, 2);

if Rp<800
    if Cp<700
        object_grey = double(rgb2gray(object_im));
        object_grey = imresize(object_grey,n1);
        big_grey = double(rgb2gray(big_im));
        big_grey = imresize(big_grey,n1);
        flag = 0;
    else
        object_grey = double(rgb2gray(object_im));
        object_grey = imresize(object_grey,n3);
        big_grey = double(rgb2gray(big_im));
        big_grey = imresize(big_grey,n3);
        flag = 1;   
    end
else
    object_grey = double(rgb2gray(object_im));
    object_grey = imresize(object_grey,n2);
    big_grey = double(rgb2gray(big_im));
    big_grey = imresize(big_grey,n2);
    flag = 2;
end
%object_im = Object image that needs to be detected
%big_im = Image in which detections needs to be done.


Ro = size(object_grey, 1);
Co = size(object_grey, 2);

Rb = size(big_grey, 1);
Cb = size(big_grey, 2);

r=0;c=0;
R_crop = 0;
R = 0;


%object_grey = double(rgb2gray(object_im));
%big_grey = double(rgb2gray(big_im));
for i = 1:Cb-Co
    for j = 1:Rb-Ro
        crop_arr = big_grey(j:j-1+Ro,i:i-1+Co);
        crop_arr = crop_arr - sum(sum(crop_arr))/numel(crop_arr);
        object_grey = object_grey - sum(sum(object_grey))/numel(object_grey);
        %object_grey = object_grey - mean2(object_grey);
        R_crop = sum(sum(object_grey.*crop_arr))/(sum(sum(object_grey.*object_grey))*sum(sum(crop_arr.*crop_arr)))^0.5;
        %R = corr2(object_grey,crop_arr);
        if R_crop >0.9
            if flag <1
                r = j/n1;
                c = i/n1;
                break
            else 
                if flag == 1
                    r = j/n3;
                    c = i/n3;
                    break
                else
                    r = j/n2;
                    c = i/n2;
                    break
                end
            end
        end
     end
end
return;
end

