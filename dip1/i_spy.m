% Please edit this function only, and submit this Matlab file in a zip file
% along with your PDF report

function [r,c] = i_spy (object_im, big_im)
Rp = size(big_im, 1);
Cp = size(big_im, 2);

if Rp<700
    if Cp<700
        object_grey = double(rgb2gray(object_im));
        object_grey = imresize(object_grey,0.6);
        big_grey = double(rgb2gray(big_im));
        big_grey = imresize(big_grey,0.6);
        flag = 0;
    end
else
    object_grey = double(rgb2gray(object_im));
    object_grey = imresize(object_grey,0.25);
    big_grey = double(rgb2gray(big_im));
    big_grey = imresize(big_grey,0.25);
    flag = 1;
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

for i = 1:Rb-Ro
    for j = 1:Cb-Co
        crop_arr = big_grey(i:i-1+Ro,j:j-1+Co);
        crop_arr = crop_arr - sum(sum(crop_arr))/numel(crop_arr);
        object_grey = object_grey - sum(sum(object_grey))/numel(object_grey);
        %object_grey = object_grey - mean2(object_grey);
        R_crop = sum(sum(object_grey.*crop_arr))/(sum(sum(object_grey.*object_grey))*sum(sum(crop_arr.*crop_arr)))^0.5;
        %R = corr2(object_grey,crop_arr);
        if R_crop >0.9
            if flag == 0
                r = i/0.6;
                c = j/0.6;
                break
            else    
                r = i/0.25;
                c = j/0.25;
                break
            end
        end
     end
end
return;
end

