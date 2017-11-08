function get_region(filename,t_ex,dt)
% The function is used to extract region in the single-molecule
% trajectories for further data analysis.
% filename
% t_ex:   The time region to be excluded. t(1) start; t(2) end
% dt: Time interval in the data file in ms.
%  get_region ('JUN1616_S0', [0,40],0.2e-3)
close all;
load(filename)
[th, ext, force, trap_sep, Avt]=tweezer_filter(filename,dt);
index=false(size(th));
if max(th)<t_ex(2)
    return
end
ind=th>t_ex(1) & th<t_ex(2);
index(ind)=true;
Force=force(index);
Ext=ext(index);
ext_min=min(Ext);
ext_1=Ext-ext_min;
EXT_FORCE=[ext_1,Force];
newfilename=[filename '_nonsig'];
plot(ext_1,Force);
xlabel('DNA extension (nm)');
ylabel('Force (pN)');
title([filename ', Force-extension' ', Average time= ' num2str(Avt) ' ms']);
saveas(gcf,[newfilename,'.png']);
save(newfilename,'basefilename', 'EXT_FORCE')
disp('Data excluding the following regions')
disp(t_ex)
disp(['has been deleted from ' filename])
disp(['and saved in file ' newfilename])
return