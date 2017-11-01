function process(filename,t_ex,dt)
% The function process all files listed in a txt file named filename
% The data will be extracted by get_region.m
% with t_ex limits the time range and dt denotes the average time
% window(ms)
fileID = fopen(filename);
allfile=textscan(fileID,'%s');
fclose(fileID);
n=size(allfile{1},1);
for i=1:n
    file=allfile{1}{i}
    get_region(file,t_ex,dt)
end


return