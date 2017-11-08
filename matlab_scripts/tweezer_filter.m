function [th, ext, force, trap_sep, Avt]=tweezer_filter(filename,avtime)
% This function is used to filter the tweezer time trajectories using a
% time window around avtime.
% Input
% filename: name of the file containing the original tweezer data in 0.mat
%           format.
% avtime: Approximate time windown used for the mean-filtering

% Output:
% th: the filtered time
% ext: extension
% force: force
% Avt: the actual time window used in the mean-filtering
load(filename)

global basefilename av cal p_DNA K_DNA force ext trap_sep th

Nt=length(av.ac.ext);
% No filtering. Make a time-array in secs
th=zeros(size(av.ac.ext));
th=(0:Nt-1)'+0.5;
th=th.*(cal.avtime/1000); 
% input window size in ms for filtering data. If no window size input, Avt
% will be NaN.
Avt=avtime; 
if(~isnan(Avt))
    % Moving-box averaging
    winsize=round(Avt/cal.avtime); % Number of data points in winsize
    if(mod(winsize,2)==0);
       % If winsize is not odd, convert to odd
       winsize=winsize+1;
    end
    Avt=winsize.*cal.avtime;  % Actuall window size
    th=reduce_filter1(th,winsize);
    % Note that force is up shift by 1 pN
    force=reduce_filter1(av.d.avforce,winsize)+1;
    ext=reduce_filter1(av.ac.ext,winsize);
    trap_sep=reduce_filter1(av.d.trapsep,winsize);
else
    % No filtering
    force=av.d.avforce+1;
    ext=av.ac.ext;
    trap_sep=av.d.trapsep; 
    Avt=cal.avtime;
end

return