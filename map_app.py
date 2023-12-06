from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def map_page():
    violation_number = []
    velocity = []
    coordinates = []
    # Read coordinates from velocity violation file
    with open('velocity_violations.txt', 'r') as file:
        for l in file:
            line = l.strip()

            violation_start_index = line.find('#') + 1
            violation_end_index = line.find(':')
            violation_number.append(int(line[violation_start_index:violation_end_index]))

            coord_start_ind = line.find('(') + 1
            coord_end_ind = line.find(')') 

            coordinate = line[coord_start_ind:coord_end_ind]
            coordinate = coordinate.replace(" ", "")
            coordinates.append(coordinate)

            velocity_start_index = coord_end_ind + 3
            velcity_end_index = line.find(' m/s')
            velocity.append(float(line[velocity_start_index:velcity_end_index]))
        
        # coordinates = [line.strip() for line in file]

    # Pass coordinates to the template
    print(violation_number)
    print(velocity)
    return render_template('map.html', coordinates=coordinates, violation_number=violation_number, velocity=velocity)

if __name__ == '__main__':
    app.run(debug=True)
