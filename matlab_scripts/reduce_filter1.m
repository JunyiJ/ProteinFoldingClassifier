 function y1=reduce_filter1(y0,winsize)
 % Winsize in terms of data point
 if(winsize==1)
     y1=y0;
 else
      N=length(y0);
      m=floor(N/winsize);
      Nnew=m*winsize;
      [nr,nc]=size(y0);
      if(nr>1)
          y1=zeros(m,1);
      else
          y1=zeros(1,m);
      end
      for i=1:winsize
          y1=y1+y0(i:winsize:Nnew);
      end
      y1=y1./winsize;
 end


