displayVis = true;

folder_name = 'data/';
setN = [1 2];                   % Number of sets in train [1 2]
totalFramesInSets = [250 232];%[250 232];  % Total number of frames in set1 and set2
timeLimitPerFrame = 60;         % 60 seconds per frame
distThresh = [110 90 70 50];    % Distance threshold for scoring
points = 0;

for i = setN
    % Load the GT file. Order of values in GT: rho1, theta1, rho2, theta2
    gt = csvread(sprintf('%sset%d_gt.csv', folder_name, i));
    
    for j = 1 : totalFramesInSets(i)
        % Load frame
        img = imread(sprintf('%sset%d_f%05d.png', folder_name, i, j));
        
        % Start timer
        t = cputime;

        % Run algorithm
        [algRho1, algTheta1, algRho2, algTheta2] = detect_lanes(img);
        
        % Stop timer
        executionTime = cputime - t;
        
        if executionTime > timeLimitPerFrame
            fprintf(['Set %d - Frame %d. Took > %d seconds [%d]. ',...
                'Point [%d], Total Points [%d]\n'],...
                i, j, executionTime, newPoints, points);
            continue;
        end
        
        % Calculate x-values for y = 1 and y = 480 for:
        % lane1 -> rho1, theta1
        % lane2 -> rho2, theta2
        
        alg_x(1,1) = compute_x_rad(1, algRho1, algTheta1);
        alg_x(1,2) = compute_x_rad(1, algRho2, algTheta2);
        alg_x(2,1) = compute_x_rad(480, algRho1, algTheta1);
        alg_x(2,2) = compute_x_rad(480, algRho2, algTheta2);
        
        gt_x(1,1) = compute_x_rad(1, gt(j,1), gt(j,2));
        gt_x(1,2) = compute_x_rad(1, gt(j,3), gt(j,4));
        gt_x(2,1) = compute_x_rad(480, gt(j,1), gt(j,2));
        gt_x(2,2) = compute_x_rad(480, gt(j,3), gt(j,4));
        
        % Compute the differences
        for k = 1 : 2
            d1 = abs(gt_x(k,1) - alg_x(k,1));
            d2 = abs(gt_x(k,1) - alg_x(k,2));
            if(d1 < d2)
                % matched (k,1) -> (k,1) and (k,2) -> (k,2)
                dv(1+(k-1)*2) = d1;
                dv(2+(k-1)*2) = abs(gt_x(k,2) - alg_x(k,2));
            else
                % matched (k,1) -> (k,2) and (k,2) -> (k,1)
                dv(1+(k-1)*2) = d2;
                dv(2+(k-1)*2) = abs(gt_x(k,2) - alg_x(k,1));
            end
        end
        
        newPoints = 4;
        for k = 1 : 4
            pt = sum(distThresh >= dv(k));
            if pt < newPoints
                newPoints = pt;
            end
        end
        points = points + newPoints;
        
        % Visualization
        if displayVis
            figure(1); imshow (img);
            hold on;
            plot ( [gt_x(1,1) gt_x(2,1)], [1, 480], '-g' );
            plot ( [gt_x(1,2) gt_x(2,2)], [1, 480], '-g' );

            plot ( [alg_x(1,1) alg_x(2,1)], [1, 480], '-r' );
            plot ( [alg_x(1,2) alg_x(2,2)], [1, 480], '-r' );
            
            title({...
                sprintf('Set %d - Frame %d', i, j),...
                sprintf('Distance [%.0f, %.0f, %.0f, %.0f] = points [%d, %d]', ...
                dv(1), dv(2), dv(3), dv(4), ...
                newPoints, points)});
            drawnow;
            pause(0.25);
            hold off;
        end

        fprintf ( 'Set %d - frame %d.  Distance [%.0f, %.0f, %.0f, %.0f]. Point [%d], Total Points [%d]\n', ...
            i, (j-1), dv(1), dv(2), dv(3), dv(4), ...
            newPoints, points );
        
    end
end

function [x] = compute_x_rad(y, rho, theta)
    x = (rho - y*sin(theta))/cos(theta);
end