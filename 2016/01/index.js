/* eslint-env: node */

class Point {
  constructor(x, y, heading) {
    this.x = parseInt(x, 10);
    this.y = parseInt(y, 10);
    this.heading = parseInt(heading, 10);
  }

  equals(b, includeHeading = false) {
    if (this.x !== b.x) {
      return false;
    }
    if (this.y !== b.y) {
      return false;
    }
    if (includeHeading && this.heading !== b.heading) {
      return false;
    }
    return true;
  }

  distanceFrom(b) {
    return (Math.abs(b.x - this.x) + Math.abs(b.y - this.y));
  }

  static dejaVu(location, points) {
    points.forEach((p) => {
      if (location.equals(p)) {
        const d = location.distanceFrom(points[0]);
        console.log(`Been here before. We are ${d} blocks away`);
        throw new Error('Done');
      }
    });
  }

  static turn(start, direction) {
    let result = start.heading;
    switch (direction.toUpperCase()) {
      case 'R':
        result = start.heading + 90;
        break;
      case 'L':
        result = start.heading - 90;
        break;
      default:
        throw new Error('direction must be either R or L');
    }

    if (result === 360) {
      result = 0;
    } else if (result === -90) {
      result = 270;
    }
    return new Point(start.x, start.y, result);
  }

  static move(start, step, waypoints) {
    const cleanStep = step.trim();
    const direction = cleanStep[0];
    const distance = parseInt(cleanStep.slice(1), 10);
    let position = Point.turn(start, direction);

    for (let i = 0; i < distance; i += 1) {
      switch (position.heading) {
        case 0:
          position = new Point(position.x, position.y + 1, position.heading);
          break;
        case 90:
          position = new Point(position.x + 1, position.y, position.heading);
          break;
        case 180:
          position = new Point(position.x, position.y - 1, position.heading);
          break;
        case 270:
          position = new Point(position.x - 1, position.y, position.heading);
          break;
        default:
          throw new Error('heading is invalid. Must be 0, 90, 180, or 270');
      }
      if (Point.dejaVu(position, waypoints)) {
        throw new Error('Done');
      }
      waypoints.push(position);
    }
    return position;
  }
}

//const directions = 'R8, R4, R4, R8';
const directions = 'R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2';
const steps = directions.split(',');

console.log(`There are ${steps.length} steps.`);

const start = new Point(0, 0, 0);
let location = start;
let distance = 0;
const waypoints = [start];

try {
  steps.forEach((step) => {
    location = Point.move(location, step, waypoints);
  });
} catch (e) {
  console.log(e);
}

distance = location.distanceFrom(start);

console.log(`Distance from start: ${distance}`);
