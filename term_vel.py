import matplotlib.pyplot as plt
import numpy as np
import plt_config


#Velocity of a cyclist riding downhill, beginning at rest
def vel_function(m, theta, CDA, t):
    return term_vel_function(m, theta, CDA) * np.tanh(np.sqrt((9.8*1.2*CDA*np.sin(theta))/(2*m))*t)

#Terminal Velocity of a cyclist riding downhill
def term_vel_function(m, theta, CDA):
    return np.sqrt((2*m*9.8*np.sin(theta))/(1.2*CDA))


#Plots terminal velocity as a function of rider's CDA and hill's grade
def plot_term_vel(grade, CDAs):

    theta = np.arctan(grade/100)

    m = np.linspace(0, 140, 300)

    colors = ['red', 'orange', 'green', 'cyan', 'blue', 'purple']
    
    for i, CDA in enumerate(CDAs):
        y = term_vel_function(m, theta, CDA)

        m_lb = m*2.20462
        y_mph = y*(3600/1609.34)

        plt.plot(m_lb, y_mph, label=f"CDA={CDA:.2f}", color=colors[i])

    plt.grid()
    plt.title(f"{grade}% Grade")
    plt.ylim(top=120)
    plt.yticks([0, 25, 50, 75, 100])
    plt.xlabel(r"$m$ (lb)")
    plt.ylabel(r"$v_T$ (mi/hr)")
    plt.legend(ncol=2)
    plt.tight_layout()
    plt.savefig(f"term_vel/cyclist_term_vel_grade={grade}.png")
    plt.close()


#Plots velocity as a function of time and hill's grade
def plot_vel(grade, masses):

    theta = np.arctan(grade/100)
    CDA = 0.3

    t = np.linspace(0, 200, 300)

    colors=['deeppink', 'orangered', 'gold', 'turquoise', 'royalblue', 'darkviolet']

    for i, m in enumerate(masses):
        y = vel_function(m, theta, CDA, t)

        y_mph = y*(3600/1609.34)
        t_min = t/60

        plt.plot(t_min, y_mph, label=f"m={m*2.20462:.0f} lb", color=colors[i])
        v_T = term_vel_function(m, theta, CDA)*(3600/1609.34)
        plt.axhline(y=v_T, linestyle='dashed', alpha=0.3, color=colors[i])

    plt.grid()
    plt.title(f"{grade}% Grade, CDA={CDA}")
    plt.ylim(top=85)
    plt.yticks([0, 25, 50, 75])
    plt.xlabel(r"$t$ (min)")
    plt.ylabel(r"$v(t)$ (mi/hr)")
    plt.legend(ncol=2)
    plt.tight_layout()
    plt.savefig(f"vel/cyclist_vel_grade={grade}_CDA={CDA}.png")
    plt.close()


for grade in np.linspace(2, 24, num=12):

    CDAs = np.linspace(0.2, 0.4, num=6) #Sets list of rider CDAs (drag coefficient x frontal area) to compare
    plot_term_vel(int(grade), CDAs) #Generates Fig 2

    masses = np.linspace(50, 100, num=6)
    plot_vel(int(grade), masses) #Generates Fig 3
