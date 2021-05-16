from carbonserver.database import schemas, models

import abc
from typing import List


class Experiments(abc.ABC):
    @abc.abstractmethod
    def add_experiment(self, experiment: schemas.ExperimentCreate):
        raise NotImplementedError

    @abc.abstractmethod
    def get_db_to_class(self, experiment: models.Experiment) -> schemas.Experiment:
        raise NotImplementedError

    @abc.abstractmethod
    def get_one_experiment(self, experiment_id):
        raise NotImplementedError

    @abc.abstractmethod
    def get_experiments_from_project(self, project_id) -> List[schemas.Experiment]:
        raise NotImplementedError
