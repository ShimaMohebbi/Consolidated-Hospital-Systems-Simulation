import pandas as pd
import numpy as np


class HospitalInfo:

    def __init__(self):
        self.physician = ["DR henry", "DR Jack", "DR boo", "Dr lolo", "Dr Libman", "Dr Niptuk"]
        self.hospitals = ['Chicago', 'Milwaukee', 'Springfield']
        self.services = ["Cardiology", "Oncology"]
        self.hospitals_service = pd.DataFrame(data=np.array([[1, 1, 0], [0, 1, 1]]).T,
                                              index=self.hospitals, columns=self.services)
        self.physician_hospital_service = pd.DataFrame(data=np.array([[0, 0, 0, 1, 0, 0],
                                                                      [1, 0, 0, 0, 0, 0],
                                                                      [0, 0, 1, 0, 0, 0],
                                                                      [0, 0, 1, 0, 0, 0],
                                                                      [0, 0, 0, 0, 1, 0],
                                                                      [0, 0, 0, 0, 0, 1]
                                                                      ]).T,
                                                       index=pd.MultiIndex(
                                                           levels=[self.hospitals, self.services],
                                                           labels=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]]
                                                       ),
                                                       columns=self.physician)

        self.cost_loosing_patient = pd.DataFrame(np.random.randint(200,
                                                                   1000,
                                                                   size=(len(self.hospitals), len(self.services))
                                                                   ),
                                                 index=self.hospitals, columns=self.services)
        for i in self.hospitals:
            for j in self.services:
                if self.hospitals_service.loc[i, j] == 0:
                    self.cost_loosing_patient.loc[i, j] = 500000

        self.bed_hospital = pd.DataFrame(np.random.randint(0, 1000, size=(1, len(self.hospitals))),
                                         columns=self.hospitals)

    def physician_request(self, specialty):
        idx = pd.IndexSlice
        data = self.physician_hospital_service[self.physician_hospital_service.loc[idx[:, specialty], :]>0.5]
        unic= data.apply(pd.Series.nunique)
        data=data.drop(unic[unic==0].index,axis=1)
        return data.columns.values