function get_region(filename,t_ex,dt)
% The function is used to extract region in the single-molecule
% trajectories for further data analysis.
% filename
% t_ex:   The time region to be excluded. t(1) start; t(2) end
% dt: Time interval in the data file in second.
%  get_region ('JUN1616_S0', [0,40],0.2e-3)

load(filename)
index=false(size(av.d.time));
m=dt./mean(diff(av.d.time(1:10)));
ind=av.d.time>t_ex(1) & av.d.time<t_ex(2);
index(ind)=true;

av.d.time=av.d.time(index);
av.d.avforce=av.d.avforce(index);
av.d.trapsep=av.d.trapsep(index);
av.ac.ext=av.ac.ext(index);
ext_min=min(av.ac.ext);
ext_1=av.ac.ext-ext_min;
EXT_FORCE=[ext_1,av.d.avforce];
newfilename=[filename '_nonsig'];
plot(ext_1,force_1,ext_1,forcen{ns});
save(newfilename,'basefilename', 'EXT_FORCE')
disp('Data excluding the following regions')
disp(t_ex)
disp(['has been deleted from ' filename])
disp(['and saved in file ' newfilename])
return