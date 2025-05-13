interface Configuration {
    site: {
        title: string,
        theme?: string
    }
}


declare module "*.yml" {
    const value: Configuration;
    export default value;
}