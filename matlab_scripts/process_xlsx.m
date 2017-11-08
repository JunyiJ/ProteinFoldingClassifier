function process_xlsx(filename,sheet,range,t_ex,dt)
%Generate a txt file containing the filenames needed.
%filename is the name of a spread sheet
%sheet specifys which sheet should be used
%range, for example 'B2:C162'
%t_ex, time start and stop for example [0,40]
%average time window (ms) 0.2
% for example> process_xlsx('vSNARE.xlsx','Yeast SNARE only','C2:C162',[0,40],0.2)

[num,txt,raw] = xlsread(filename,sheet,range);
strs = txt(~cellfun('isempty',txt));
n=size(strs,1);
for i=1:n
    file=strs{i}
    try
        get_region(file,t_ex,dt);
    end
end
end