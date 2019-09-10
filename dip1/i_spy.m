% Please edit this function only, and submit this Matlab file in a zip file
% along with your PDF report

function [r,c] = i_spy (object_im, big_im)
%object_im = Object image that needs to be detected
%big_im = Image in which detections needs to be done.

Ro = size(object_im, 1);
Co = size(object_im, 2);

Rb = size(big_im, 1);
Cb = size(big_im, 2);

r=0;c=0;
R_crop = 0;
R = 0;

object_grey = double(rgb2gray(object_im));
big_grey = double(rgb2gray(big_im));
for i = 1:Rb-Ro
    for j = 1:Cb-Co
        crop_arr = big_grey(i:i-1+Ro,j:j-1+Co);
        crop_arr = crop_arr - sum(sum(crop_arr))/numel(crop_arr);
        object_grey = object_grey - sum(sum(object_grey))/numel(object_grey);
        %object_grey = object_grey - mean2(object_grey);
        R_crop = sum(sum(object_grey.*crop_arr))/(sum(sum(object_grey.*object_grey))*sum(sum(crop_arr.*crop_arr)))^0.5;
        %R = corr2(object_grey,crop_arr);
        if R_crop >0.95
            r = i;
            c = j;
            break

        end
     end
end
return;
end
