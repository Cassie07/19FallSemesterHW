function [rho1, theta1, rho2, theta2] = detect_lanes(img)
R = size(img,1);
C = size(img,2);

% 1. Gaussion Blur
frame = imgaussfilt3(img);
%figure('Name','Gaussion filter'), imshow(frame);

% 2. White Color Mask
gray = rgb2gray(frame);
White = (gray >= 120 & gray <= 255);
%figure('Name','White Mask'), imshow(White);

% Yellow Color Mask
channel1MinY = 130;
channel1MaxY = 255;

channel2MinY = 130;
channel2MaxY = 255;

channel3MinY = 0;
channel3MaxY = 130;

Yellow=((frame(:,:,1)>=channel1MinY)&(frame(:,:,1)<=channel1MaxY))& ...
    (frame(:,:,2)>=channel2MinY)&(frame(:,:,2)<=channel2MaxY)&...
    (frame(:,:,3)>=channel3MinY)&(frame(:,:,3)<=channel3MaxY);

%figure('Name','Yellow Mask'), imshow(Yellow);

% 3. Canny Edge Detection
frameW = edge(White, 'canny', 0.2);
frameY = edge(Yellow, 'canny', 0.2);
%figure('Name','Edge Detection of Yellow mask'), imshow(frameY);
%figure('Name','Edge Detection of White mask'), imshow(frameW);

% 4. ROI
%[r c] = ginput(4)
r = [0.4*C 0.45*C 0.4*C 0.3*C];
c = [0.4*R 0.4*R 0.75*R 0.75*R];
roiY = roipoly(frameY, r, c);
[R , C] = size(roiY);
for i = 1:R
    for j = 1:C
        if roiY(i,j) == 1
            frame_roiY(i,j) = frameY(i,j);
        else
            frame_roiY(i,j) = 0;
        end
    end
end
%figure('Name','ROI from Yellow mask'), imshow(frame_roiY);

r = [0.5*C 0.56*C 0.75*C 0.5*C];
c = [0.4*R 0.4*R 0.75*R 0.75*R];
roiW = roipoly(frameW, r, c);
[R , C] = size(roiW);
for i = 1:R
    for j = 1:C
        if roiW(i,j) == 1
            frame_roiW(i,j) = frameW(i,j);
        else
            frame_roiW(i,j) = 0;
        end
    end
end
%figure('Name','ROI from White mask'), imshow(frame_roiW);

% 5. Hough Transform

[H_Y,theta_Y,rho_Y] = hough(frame_roiY);
[H_W,theta_W,rho_W] = hough(frame_roiW);

% Hough Peaks

P_Y = houghpeaks(H_Y,2,'threshold',2);
P_W = houghpeaks(H_W,2,'threshold',2);

% Hought Lines

lines_Y = houghlines(frame_roiY,theta_Y,rho_Y,P_Y,'FillGap',3000,'MinLength',20);

lines_W = houghlines(frame_roiW,theta_W,rho_W,P_W,'FillGap',3000,'MinLength',20);

rho2 = lines_Y(2).rho;
theta2 = deg2rad(lines_Y(2).theta);
rho1 = lines_W(1).rho;
theta1 = deg2rad(lines_W(1).theta);

%rho1 = 400;
%theta1 = pi/5;
%rho2 = 200;
%theta2 = -pi/6;


end