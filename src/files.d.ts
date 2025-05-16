interface Configuration {
    site: {
        title: string,
        theme?: string,
        themePicker: "enabled" | "disabled"
    }
}


declare module "*.yml" {
    const value: Configuration;
    export default value;
}