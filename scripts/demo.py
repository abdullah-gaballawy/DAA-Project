"""Demonstration entry point: fails transparently until solvers exist."""
from eed461.tasks.task_01_coin_removal import removeCoins

if __name__=='__main__':
    print('EED461 project: Task 01 demo input n=1, coins=[H]')
    try:
        print('Output:', removeCoins(1,['H']))
    except NotImplementedError as exc:
        print('NOT READY:',exc)
        print('Replace this placeholder with the final 8-task demo after implementations.')
