import numpy as np
import scipy.io as sio

def get_data(subject, training, PATH):
    NO_channels = 3
    NO_tests = 6*10
    Window_Length = 7*250

    class_return = np.zeros(NO_tests)
    data_return = np.zeros((NO_tests, NO_channels, Window_Length))

    NO_valid_trial = 0
    if training:
        a = sio.loadmat(PATH+'B0'+str(subject)+'T.mat')
    else:
        a = sio.loadmat(PATH+'B0'+str(subject)+'E.mat')
    a_data = a['data']
    for ii in range(0,a_data.size):
        a_data1 = a_data[0,ii]
        a_data2 = [a_data1[0,0]]
        a_data3 = a_data2[0]
        a_X         = a_data3[0]
        a_trial     = a_data3[1]
        a_y         = a_data3[2]
        a_fs        = a_data3[3]
        a_classes   = a_data3[4]
        a_artifacts = a_data3[5]
        a_gender    = a_data3[6]
        a_age       = a_data3[7]
        for trial in range(0, a_trial.size):
            if(a_artifacts[trial]==0):
                data_return[NO_valid_trial,:,:] = np.transpose(a_X[int(a_trial[trial]):(int(a_trial[trial])+Window_Length),:3])
                class_return[NO_valid_trial] = int(a_y[trial])
                NO_valid_trial +=1
    return data_return[0:NO_valid_trial,:,:], class_return[0:NO_valid_trial]