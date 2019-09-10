%%%%%%%%%%%%%% Note %%%%%%%%%%%%%%%%%%%
% Do not change anything in this file 
% Use part I to test your i_spy.m code on given data.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%% Part -I %%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

folder_name = 'data/'; 

setN = 3;
objectI0 = 1; 
objectI1 = 10;
distantT = 5;

timeLimitSec = 60;

t = cputime;


pt = 0;

for i = 1:setN
    fn = sprintf ( '%sset%d_big_im.png',folder_name, i );
    b_im = imread ( fn );
    
    fn = sprintf ( '%sset%d_gt.csv', folder_name, i );
    gt = csvread ( fn );
    
    for j = objectI0:objectI1
        fn = sprintf ( '%sset%d_object_im_%d.png',folder_name, i, j );
        o_im = imread ( fn );
        [r,c] = i_spy ( o_im, b_im);
        
        error_dist = sqrt( ( gt(j,1) - r ) ^ 2 + ( gt(j,2) - c ) ^ 2 );            
            
        if ( (cputime-t) >= timeLimitSec )
            fprintf ( 'final points = %d\n', pt );
            return;
        else
            if ( error_dist <= distantT )
                pt = pt + 1;
            end

            fprintf ( '%d,%d - alg(%d,%d) vs gt(%d,%d) - %f sec -> total pt [%d]\n', ...
                i, j, r, c, gt(j,1), gt(j,2), cputime-t, pt );
        end
    end
end

