% 37 version
% Write your implementation in this file.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Make sure this file returns below things to main.m
%1.top left corner coordinates(x,y),
%2.width,
%3.height
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [sx, sy, sWidth, sHeight] = auto_crop ( f )

%getting size of the input image
Ro = size(f,1);
Co = size(f,2);
grey_f = rgb2gray(f);

%imshow(erode)

%imshow(erode)
% OTSU
%[counts,x] = imhist(erode,125);
%stem(x,counts);
%T = otsuthresh(counts);
%T = adaptthresh(erode,0.65);
%BW = imbinarize(erode,T);
level = graythresh(grey_f);
BW = imbinarize(grey_f,level); %B
se = strel('arbitrary',10);
dilated = imdilate(BW,se);
se = strel('arbitrary',20);
BW = imerode(dilated,se);
%imshow(BW)
%mask = zeros(size(f));
%mask(25:end-25,25:end-25) = 1;
%bw = activecontour(f, mask, 5, 'edge');
sx = Co;
sy = Ro;
sWidth = 0;
sHeight = 0;
a = 0.6;
for i = 1:Ro %y
    tmp_sx = Co;
    tmp_sy = Ro;
    tmp_sWidth = 0;
    n_bw = 0;
    n_fw = 0;
    new = 0;
    ori_sWidth = 0;
    for j = 1:Co %x
        if BW(i,j) == 1
            n_fw = n_fw + 1;
            if j>109 && i>250 && i<Ro*0.8
                tmp_sWidth = tmp_sWidth + 1;
                if j < tmp_sx
                    tmp_sx = j;
                end

                if i < tmp_sy
                    tmp_sy = i;
                end
            end

        else
            if j-1>0 && BW(i,j-1) == 1 && tmp_sWidth < Co*0.1
                        tmp_sx = Co;
                        tmp_sy = Ro;
            end
            n_bw = n_bw + 1;
        end
    end

    if n_bw/(n_fw + n_bw) < 0.5
        tmp_a = tmp_sWidth/Co;
        if tmp_sWidth/Co > 0.2
            if tmp_a >= a
                a = tmp_a;
                if tmp_sx < sx && tmp_sx > 109
                    sx = tmp_sx;
                end
                if tmp_sy < sy && tmp_sy > 250
                    sy = tmp_sy;
                end
            end

            %if tmp_sy < sy
            %    sy = tmp_sy;
            %end

            if tmp_sWidth > sWidth
                %if tmp_sWidth > 0.9*Co
                %    ori_sWidth = tmp_sWidth;
                %    sWidth = 0.8*tmp_sWidth;
                %else
                %    ori_sWidth = tmp_sWidth;
                sWidth = tmp_sWidth;
                %end
            end
            sHeight = sHeight + 1;
        end
    end
end

sums = sx+sWidth;
if sums > Co || sums == Co
    sWidth = 0.8*sWidth;
end