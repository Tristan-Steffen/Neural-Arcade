# Use an official node image as the base image
FROM node:14-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
ADD package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
ADD . .

# Build the React app
RUN npm run build

# Install serve to serve the build
RUN npm install -g serve

# Set the environment variable to production
ENV NODE_ENV=production

# Expose the port serve runs on
EXPOSE 5000

# Serve the build folder
CMD ["serve", "-s", "build", "-l", "5000"]
