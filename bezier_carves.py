# -*- coding: utf-8 -*-

from matplotlib import pyplot

def get_point(P0, P1, t):
    L = {'x': 0.0, 'y':0.0}

    L['x'] = ((1 - t) * P0['x']) + (t * P1['x'])
    L['y'] = ((1 - t) * P0['y']) + (t * P1['y'])

    return L

if __name__ == '__main__':
    """
    P1, P2の座標を変更してベジェ曲線を理解しよう!!!
    範囲は0.0〜1.0の間がいいよ!!!
    """
    P0 = {'x':0.0, 'y':1.0}
    P1 = {'x':0.0, 'y':0.5}
    P2 = {'x':1.0, 'y':0.5}
    P3 = {'x':1.0, 'y':0.0}

    B01 = {'x': [], 'y': []}
    B12 = {'x': [], 'y': []}
    B012 = {'x': [], 'y': []}
    B23 = {'x': [], 'y': []}
    B123 = {'x': [], 'y': []}
    B0123 = {'x': [], 'y': []}


    dotsNum = 30
    # three points
    for i in range(dotsNum+1):
        pos = get_point(P0, P1, i/dotsNum)
        B01['x'].append(pos['x'])
        B01['y'].append(pos['y'])
    print('B01', B01)

    for i in range(dotsNum+1):
        pos = get_point(P1, P2, i/dotsNum)
        B12['x'].append(pos['x'])
        B12['y'].append(pos['y'])
    print('B12', B12)

    for i in range(dotsNum+1):
        B01_ce = {'x':B01['x'][i], 'y':B01['y'][i]}
        B12_ce = {'x':B12['x'][i], 'y':B12['y'][i]}
        pos = get_point(B01_ce, B12_ce, i/dotsNum)
        B012['x'].append(pos['x'])
        B012['y'].append(pos['y'])
    print('B012', B012)

    for i in range(dotsNum+1):
        pos = get_point(P2, P3, i/dotsNum)
        B23['x'].append(pos['x'])
        B23['y'].append(pos['y'])
    print('B23', B23)

    for i in range(dotsNum+1):
        B12_ce = {'x':B12['x'][i], 'y':B12['y'][i]}
        B23_ce = {'x':B23['x'][i], 'y':B23['y'][i]}
        pos = get_point(B12_ce, B23_ce, i/dotsNum)
        B123['x'].append(pos['x'])
        B123['y'].append(pos['y'])
    print('B123', B123)

    for i in range(dotsNum+1):
        B01_ce = {'x':B01['x'][i], 'y':B01['y'][i]}
        B12_ce = {'x':B12['x'][i], 'y':B12['y'][i]}
        B012_ce = get_point(B01_ce, B12_ce, i/dotsNum)

        B12_ce = {'x':B12['x'][i], 'y':B12['y'][i]}
        B23_ce = {'x':B23['x'][i], 'y':B23['y'][i]}
        B123_ce = get_point(B12_ce, B23_ce, i/dotsNum)

        pos = get_point(B012_ce, B123_ce, i/dotsNum)
        B0123['x'].append(pos['x'])
        B0123['y'].append(pos['y'])
    print('B0123', B0123)

    # draw
    fig = pyplot.figure(figsize=(5,5))
    ax = fig.add_subplot(1,1,1)

    ## point
    point = ax.plot(B0123['x'], B0123['y'], label='B0123')
    point[0].set_linestyle('-')

    point = ax.plot(P0['x'], P0['y'], label='P0')
    point[0].set_marker('D')

    point = ax.plot(P1['x'], P1['y'], label='P1')
    point[0].set_marker('D')

    point = ax.plot(P2['x'], P2['y'], label='P2')
    point[0].set_marker('D')

    point = ax.plot(P3['x'], P3['y'], label='P3')
    point[0].set_marker('D')

    ## setting pyplot
    pyplot.legend()
    size = max(P1['x'], P1['y'], P2['x'], P2['y'], P3['x'], P3['y'])
    pyplot.ylim(-0.1, size+0.1)
    pyplot.xlim(-0.1, size+0.1)
    pyplot.ylabel('Y-axis')
    pyplot.xlabel('X-axis')
    pyplot.show()

