interface Configuration {
    site: {
        title: string
    }
}


declare module "*.yml" {
    const value: Configuration;
    export default value;
}