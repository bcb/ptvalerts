from ptvalerts import ptv, alerts


if __name__ == '__main__':
    disruptions = ptv.get_disruptions()
    users = (
        ptv.User('Barry', '@barry', 'Belgrave', 1),
        ptv.User('Harry', '@harry', 'Hurstbridge', 2),
        ptv.User('Wally', '@wally', 'Werribee', 3),
        ptv.User('Freddy', '@freddy', 'Frankston', 4),
    )
    alerts.send(disruptions, users)