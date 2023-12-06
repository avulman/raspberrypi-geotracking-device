from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def map_page():
    # Initialize empty lists to store data
    violation_number = []
    velocity = []
    coordinates = []
    date = []
    time = []

    # Read coordinates, violation information, date, time, and velocity from the velocity violation file
    with open('velocity_violations.txt', 'r') as file:
        for l in file:
            line = l.strip()

            # Extract violation number from the line
            violation_start_index = line.find('#') + 1
            violation_end_index = line.find(':')
            violation_number.append(int(line[violation_start_index:violation_end_index]))

            # Extract coordinates from the line
            coord_start_ind = line.find('(') + 1
            coord_end_ind = line.find(')') 
            coordinate = line[coord_start_ind:coord_end_ind]
            coordinate = coordinate.replace(" ", "")
            coordinates.append(coordinate)

            # Extract date information from the line
            d_start_index = line.find(':') + 2
            d_end_index = d_start_index + 10
            date.append(line[d_start_index:d_end_index])

            # Extract time information from the line
            t_start_index = d_end_index + 1
            t_end_index = line.find('.')
            time.append(line[t_start_index:t_end_index])

            # Extract velocity information from the line
            velocity_start_index = coord_end_ind + 3
            velocity_end_index = line.find(' m/s')
            mps_velocity = float(line[velocity_start_index:velocity_end_index])

            # Convert m/s velocity to miles per hour
            miph = mps_velocity * 60 * 60 / 1609.34
            miph = round(miph, 2)
            velocity.append(miph)

    # Pass data to the template for rendering
    print(violation_number)
    print(velocity)
    return render_template('map.html', coordinates=coordinates, violation_number=violation_number, date=date, time=time, velocity=velocity)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
