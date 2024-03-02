export default function pagination(info, route) {
    const is_page_exists = (direction) => {
        return isPageExists(info, direction);
    }

    const get_page_param = (direction) => {
        return getPageParam(info, route, direction);
    }

    const get_path = (direction) => {
        return getPath(info, direction);
    }
    return {
        is_page_exists,
        get_page_param,
        get_path
    }
}

function isPageExists(info, direction) {
    if (direction == 'next')
        return info.value.next !== 'null';
    return info.value.previous !== 'null';
}

function getPageParam(info, route, direction) {
    try {
        let urlString;
        switch (direction) {
            case 'next':
                urlString = info.value.next;
                break;
            case 'previous':
                urlString = info.value.previous;
                break;
            default:
                return route.query.page;
        }

        const url = new URL(urlString);
        return url.searchParams.get(page);
    }
    catch (error) {
        console.error("存在错误：", error);
        return;
    }
}

function getPath(info, direction) {
    let url = '';
    try {
        switch (direction) {
            case 'next':
                if (info.value.next !== undefined) {
                    url += (new URL(info.value.next)).search
                }
                break;
            case 'previous':
                if (info.value.previous !== undefined) {
                    url += (new URL(info.value.previous)).search
                }
                break;
        }
    } catch (error) {
        console.log('存在错误：', error);
        return url;
    }
    return url;
}