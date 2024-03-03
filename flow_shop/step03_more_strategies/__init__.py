# import reader
from flow_shop.step03_more_strategies import reader
from flow_shop.step03_more_strategies.problem import Problem


def main():
    pass
    batch = reader.read_sample_batch()
    problem = Problem(batch, time_limit=10)
    plan = problem.solve()
    problem.dump(plan)


if __name__ == '__main__':
    main()
