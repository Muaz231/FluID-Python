function wav = helperDesignFMCWWaveform(c,lambda)
% This function helperDesignFMCWWaveform is only in support of
% MIMORadarVirtualArrayExample. It may change in a future release.

% Copyright 2017 The MathWorks, Inc.

range_max = 200;
tm = 5.5*range2time(range_max,c);
range_res = 0.0375; % For BW of 4 GHz
bw = rangeres2bw(range_res,c);
% bw = 4e9; % 4 GHz bandwidth


sweep_slope = bw/tm;
fr_max = range2beat(range_max,sweep_slope,c);

v_max = 230*1000/3600;
fd_max = speed2dop(2*v_max,lambda);

fb_max = fr_max+fd_max;
fs = max(2*fb_max,bw);
% fs = Nr/tm;

% Real value parameters
BW = 4e9;
Tm = 156.56e-6;
Fs= 6700e3;
Ns = 1024;

wav = phased.FMCWWaveform('SweepTime',Ns/Fs,'SweepBandwidth',BW,...
    'SampleRate',Fs);
